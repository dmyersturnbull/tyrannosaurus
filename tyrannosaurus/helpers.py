"""
Original source: https://github.com/dmyersturnbull/tyrannosaurus
Copyright 2020–2021 Douglas Myers-Turnbull
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0

Various support code, including enums and utils.
"""

from __future__ import annotations

import logging
import os
import re
from pathlib import Path
from subprocess import SubprocessError, check_output  # nosec
from typing import Mapping, Optional, Sequence, Union
from typing import Tuple as Tup

import requests
import typer

logger = logging.getLogger(__package__)


class TrashList:
    def __init__(self, dists: bool, aggressive: bool):
        self.trash_patterns = {
            ".pytest_cache",
            ".mypy_cache",
            "__pycache__",
            "cython_debug",
            "eggs",
            "__pypackages__",
            "docs/_html",
            "docs/_build",
            re.compile(r".*\.egg-info"),
            re.compile(r".*\.py[cod]"),
            re.compile(r".*\$py\.class"),
            re.compile(r".*\.egg-info"),
        }
        if dists:
            self.trash_patterns.add("dists")
        if aggressive:
            self.trash_patterns.update(
                {
                    ".tox",
                    "poetry.lock" "docs/html",
                    "Thumbs.db",
                    "dist",
                    "sdist",
                    ".ipynb_checkpoints",
                    ".cache",
                    re.compile(r"\*\.swp"),
                    re.compile(r".*[~.]temp"),
                    re.compile(r".*[~.]tmp"),
                }
            )

    def get_list(self) -> Sequence[str]:
        return [s for s in self.trash_patterns if isinstance(s, str)]

    def get_patterns(self) -> Sequence[re.Pattern]:
        return [s for s in self.trash_patterns if isinstance(s, re.Pattern)]

    def should_delete(self, p: Path) -> bool:
        return any(
            (
                (
                    isinstance(pattern, str)
                    and str(p).replace("\\", "/").endswith(pattern)
                    or isinstance(pattern, re.Pattern)
                    and pattern.fullmatch(p.name)
                )
                for pattern in self.trash_patterns
            )
        )


class _Env:
    def __init__(self, authors: Optional[Sequence[str]], user: Optional[str]):
        self.authors = self._git("user.name", "author").split(",") if authors is None else authors
        self.user = self._git("user.email", "user").split("@")[0] if user is None else user

    def _git(self, key: str, name: str) -> str:
        try:
            result = check_output(["git", "config", key], encoding="utf8").strip()  # nosec
        except SubprocessError:
            logger.error("Failed calling git")
            return f"<<{name}>>"
        if len(result) > 0:
            return result
        else:
            logger.error(f"Could not get git config item {key}")
            return f"<<{name}>>"


class PyPiHelper:
    def new_versions(self, pkg_versions: Mapping[str, str]) -> Mapping[str, Tup[str, str]]:
        logger.warning("Making a best effort to find new versions. Correctness is not guaranteed.")
        updated = {}
        for pkg, version in pkg_versions.items():
            if pkg == "python":
                continue
            logger.debug(f"Searching pypi for package {pkg} (current version: {type(version)})")
            version = self._extract_version(version)
            if version is None:
                logger.error(f"Failed to extract version from {version} for package {pkg}")
                continue
            try:
                new = self.get_version(pkg)
            except ValueError:
                logger.error(f"Did not find package {pkg}", exc_info=True)
            except LookupError:
                logger.error(f"Failed extracting new version for pypi package {pkg}")
                logger.debug(f"Version error for {pkg}", exc_info=True)
            else:
                if new != version:
                    updated[pkg] = version, new
        return updated

    def _extract_version(self, version: str) -> Optional[str]:
        version = str(version)
        matches = re.compile(r"([0-9]+[^ ,]+)").finditer(version)
        matches = list(matches)
        if len(matches) == 0 or len(matches) > 2:
            return None
        # assume the last one will be the max if there are two
        return matches[-1].group(1)

    def get_version(self, name: str) -> str:
        pat = re.compile('"package-header__name">[ \n\t]*' + name + " ([0-9a-zA-Z_.-]+)")
        try:
            try:
                r = requests.get(f"https://pypi.org/project/{name}")
            except OSError:
                logger.debug(f"Failed fetching PyPi vr for package {name}", exc_info=True)
                r = None
            if r is None or r.status_code > 400:
                # thanks to Sphinx and a couple of others
                r = requests.get(f"https://pypi.org/project/{name.capitalize()}")
                if r.status_code > 400:
                    raise LookupError(f"Status code {r.status_code} from pypi for package {name}")
        except OSError:
            logger.error(
                f"Failed fetching {name} from pypi.org.",
                exc_info=True,
            )
            raise
        matches = {m.group(1).strip() for m in pat.finditer(r.content.decode(encoding="utf8"))}
        if len(matches) != 1:
            raise LookupError(
                f"Failed to extract version from pypi for package {name} (matches: {matches})"
            )
        return next(iter(matches))


class CondaForgeHelper:
    def has_pkg(self, name: str):
        # unfortunately, Anaconda returns 200 even if the page doesn't exist
        try:
            r = requests.get(f"https://anaconda.org/conda-forge/{name}")
        except OSError:
            logger.error(
                f"Failed fetching from anaconda.org. Assuming {name} is in Conda-Forge.",
                exc_info=True,
            )
            return True
        return "login?next" not in r.url


class EnvHelper:
    def process(self, name: str, deps, extras: bool) -> Sequence[str]:
        helper = CondaForgeHelper()
        lines = [
            "# auto-generated by `tyrannosaurus env`",
            "name: " + name,
            "channels:",
            "    - conda-forge",
            "dependencies:",
        ]
        not_in = []
        for key, value in deps.items():
            # TODO
            if not isinstance(value, str):
                if value.get("optional") is True and not extras:
                    continue
                if "extras" in value:
                    logger.error(f"'extras' not supported for {key} = {value}")
                value = value.get("version")
            # TODO handle ~ correctly
            if "^" in value or "~" in value:
                vr_pat_1 = re.compile(r"^[^~]([0-9]+)(?:\.([0-9]+))?(?:\.([0-9]+))?$")
                if (match := vr_pat_1.fullmatch(value)) is not None:
                    value = f">={match.group(1)}.{match.group(2)},<{int(match.group(1)) + 1}.0"
                else:
                    logger.error(f"Couldn't parse {key} = {value}")
            line = "    - " + key + value.replace(" ", "")
            if helper.has_pkg(key):
                lines.append(line)
            else:
                not_in.append(line)
        typer.echo(f"Found {len(not_in)} dependencies not in Conda-Forge.")
        if len(not_in) > 0:
            # TODO: hardcoded pip version
            lines.append("    - pip>=20")
            lines.append("    - pip:")
            for line in not_in:
                lines.append("    " + line)
        lines.append("")
        return lines


def scandir_fast(topdir: Union[str, Path], trash: TrashList) -> Sequence[Path]:
    """

    Args:
        topdir: The directory to search under
        trash: List of trash dirs

    """
    subdirs = [Path(f.path) for f in os.scandir(topdir) if Path(f).is_dir()]
    for dirname in list(subdirs):
        if (
            dirname.is_dir()
            and dirname.name
            not in {".tox", ".pytest_cache", ".git", ".idea", "docs", "__pycache__"}
            and dirname.name not in {str(s) for s in trash.get_list()}
        ):
            subdirs.extend(scandir_fast(dirname, trash))
    return subdirs


__all__ = [
    "TrashList",
    "_Env",
    "CondaForgeHelper",
    "PyPiHelper",
    "EnvHelper",
    "scandir_fast",
]
