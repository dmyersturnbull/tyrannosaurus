"""
Support code for Tyrannosaurus.
"""

from __future__ import annotations

import enum
import logging
import re
from pathlib import Path
from subprocess import check_output
from typing import Union, Sequence, Mapping

import requests
import typer

from tyrannosaurus.context import _Context

logger = logging.getLogger(__package__)
cli = typer.Typer()


class _SyncHelper:
    def __init__(self, context: _Context, dry_run: bool):
        self.context = context
        self.dry_run = dry_run

    def has(self, key: str):
        return self.context.has_target(key)

    def replace_substrs(self, path: Path, replace: Mapping[str, str]) -> None:
        self.context.back_up(path)
        new_lines = []
        for line in path.read_text(encoding="utf8").splitlines():
            for k, v in replace.items():
                if line.startswith(k):
                    new_lines.append(v)
                    break
            else:
                new_lines.append(line)
        new_lines = "\n".join(new_lines)
        if not self.dry_run:
            path.write_text(new_lines, encoding="utf8")
        logger.debug("Wrote to {}".format(path))

    def fix_init(self) -> None:
        if self.has("init"):
            self.replace_substrs(
                self.context.path / self.context.project / "__init__.py",
                {
                    "__status__ = ": '__status__ = "{}"'.format(self.context.source("status")),
                    "__copyright__ = ": '__copyright__ = "{}"'.format(
                        self.context.source("copyright")
                    ),
                    "__date__ = ": '__date__ = "{}"'.format(self.context.source("date")),
                },
            )

    def fix_recipe(self) -> None:
        if self.has("recipe"):
            self.replace_substrs(
                self.context.path_source("recipe"),
                {"{% set version = ": '{% set version = "' + str(self.context.version) + '" %}',},
            )


class _TrashList:
    def __init__(self, aggressive: bool):
        self.trash_patterns = {
            ".egg-info",
            ".pytest_cache",
            "__pycache__",
            "cython_debug",
            "eggs",
            "__pypackages__",
            "Thumbs.db",
            "docs/html",
            "docs/_html",
            "docs/_build",
            "dist",
            "sdist",
            re.compile(r".*\.py[cod]"),
            re.compile(r".*\$py\.class"),
            re.compile(r".*\.egg-info"),
        }
        if aggressive:
            self.trash_patterns.update(
                {re.compile(r"\*\.swp"), ".tox", ".ipynb_checkpoints", "poetry.lock"}
            )

    def get_list(self) -> Sequence[Path]:
        return [Path(s) for s in self.trash_patterns if isinstance(s, str)]

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


class _License(enum.Enum):
    apache2 = "apache2"
    cc0 = "cc0"
    ccby = "cc-by"
    ccbync = "cc-by-nc"
    gpl3 = "gpl3"
    lgpl3 = "lgpl3"
    mit = "mit"

    def full_name(self) -> str:
        return dict(apache2="Apache-2.0", mit="MIT",).get(self.name, "")


class _Env:
    def __init__(self, **kwargs):
        self.authors = kwargs.get("authors", self._git("user.name")).split(",")
        self.user = kwargs.get("user", self._git("user.email"))
        if "@" in self.user:
            self.user = self.user.split("@")[0]

    def _git(self, key: str) -> str:
        return check_output(["git", "config", key], encoding="utf8")


class _InitTomlHelper:
    def __init__(self, name: str, authors: Sequence[str], license_name, username: str):
        self.name = name
        self.authors = authors
        self.license_name = license_name
        self.username = username

    def fix(self, lines: Sequence[str]):
        new_lines = self._set_lines(
            lines,
            dict(
                name=self.name,
                version="0.1.0",
                description="A new project",
                authors=str(self.authors),
                maintainers=str(self.authors),
                license=self.license_name.full_name(),
                keywords=str(["a new", "python project"]),
                homepage="https://github.com/{}/{}".format(self.username, self.name),
                repository="https://github.com/{}/{}".format(self.username, self.name),
                documentation="https://{}.readthedocs.io".format(self.name),
                build="https://github.com/{}/{}/actions".format(self.username, self.name),
                issues="https://github.com/{}/{}/issues".format(self.username, self.name),
                source="https://github.com/{}/{}".format(self.username, self.name),
            ),
        )
        # this one is fore tool.tyrannosaurus.sources
        # this is a hack
        new_lines = self._set_lines(new_lines, dict(maintainers=self.username))
        return new_lines

    def _set_lines(self, lines: Sequence[str], prefixes: Mapping[str, Union[int, str]]):
        new_lines = []
        set_val = set()
        for line in lines:
            new_line = line
            for key, value in prefixes.items():
                if isinstance(value, str):
                    value = '"' + value + '"'
                if line.startswith(key + " = ") and key not in set_val:
                    new_line = key + " = " + value
                    set_val.add(key)
            new_lines.append(new_line)
        return new_lines


class _CondaForgeHelper:
    def has_pkg(self, name: str):
        # unfortunately, Anaconda returns 200 even if the page doesn't exist
        r = requests.get("https://anaconda.org/conda-forge/{}".format(name))
        return "You're trying to access a page that requires authentication." not in r.text


class _EnvHelper:
    def process(self, name: str, deps, extras: bool) -> Sequence[str]:
        helper = _CondaForgeHelper()
        lines = ["name: " + name, "channels:", "  -conda-forge", "dependencies:"]
        not_in = []
        for key, value in deps.items():
            # TODO
            if not isinstance(value, str):
                if value.get("optional") is True and not extras:
                    continue
                if "extras" in value:
                    logger.error("'extras' not supported for {} = {}".format(key, value))
                value = value.get("version")
            # TODO handle ~ correctly
            if "^" in value or "~" in value:
                match = re.compile(r"^[^~]([0-9]+)(?:\.([0-9]+))?(?:\.([0-9]+))?$").fullmatch(value)
                if match is not None:
                    value = (
                        ">="
                        + match.group(1)
                        + "."
                        + match.group(2)
                        + ",<"
                        + str(int(match.group(1)) + 1)
                        + ".0"
                    )
                else:
                    logger.error("Couldn't parse {}".format(key + " = =" + value))
            line = "  - " + key + value.replace(" ", "")
            if helper.has_pkg(key):
                lines.append(line)
            else:
                not_in.append(line)
        typer.echo("Found {} dependencies not in Conda-Forge.".format(len(not_in)))
        if len(not_in) > 0:
            lines.append("  - pip:")
            for line in not_in:
                lines.append("  " + line)
        lines.append("")
        return lines


__all__ = [
    "_TrashList",
    "_SyncHelper",
    "_Env",
    "_License",
    "_InitTomlHelper",
    "_CondaForgeHelper",
    "_EnvHelper",
]
