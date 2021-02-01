"""
Original source: https://github.com/dmyersturnbull/tyrannosaurus
Copyright 2020–2021 Douglas Myers-Turnbull
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0

Module that generates new projects.
"""

from __future__ import annotations

import logging
import os
import shutil
import stat
from pathlib import Path
from subprocess import CalledProcessError, check_output, PIPE  # nosec
from typing import Dict, Sequence, Union, Optional, List

import typer

from tyrannosaurus.parser import LiteralParser
from tyrannosaurus.enums import DevStatus, License

tyranno_url = "https://github.com/dmyersturnbull/tyrannosaurus.git"
logger = logging.getLogger(__package__)
cli = typer.Typer()


class VersionNotFoundError(LookupError):
    """
    The Git tag corresponding to the version was not found.
    """


class New:
    def __init__(
        self,
        name: str,
        license_name: Union[str, License],
        username: str,
        authors: Sequence[str],
        description: str,
        keywords: Sequence[str],
        version: str,
        status: DevStatus,
        should_track: bool,
        tyranno_vr: str,
        debug: bool = False,
    ):
        if isinstance(license_name, str):
            license_name = License[license_name.lower()]
        # check for historical reasons; can remove in the future
        if not isinstance(tyranno_vr, str):  # pragma: no cover
            raise ValueError(f"{tyranno_vr} has type {type(tyranno_vr)}")
        self.project_name = name.lower()
        self.pkg_name = name.replace("_", "").replace("-", "").replace(".", "").lower()
        self.license_name = license_name
        self.username = username
        self.authors = authors
        self.description = description
        self.keywords = keywords
        self.version = version
        self.status = status
        self.should_track = should_track
        self.repo_to_track = f"https://github.com/{username}/{name.lower()}.git"
        self.tyranno_vr = str(tyranno_vr)
        self.parser = LiteralParser(
            project=self.project_name,
            user=self.username,
            authors=self.authors,
            description=self.description,
            keywords=self.keywords,
            version=self.version,
            status=self.status,
            license_name=self.license_name.name,
            tyranno_vr=self.tyranno_vr,
        )
        self.debug = debug

    def create(self, path: Path) -> None:
        self._checkout(Path(str(path).lower()))
        logger.info("Got git checkout. Fixing...")
        # remove tyrannosaurus-specific files
        Path(path / "poetry.lock").unlink()
        _recipe_path = Path(path / "recipes" / "tyrannosaurus" / "meta.yaml")
        if _recipe_path.exists():
            _recipe_path.unlink()
        Path(path / "recipes" / "tyrannosaurus").rmdir()
        for p in Path(path / "docs").iterdir():
            if p.is_file() and p.name not in {"conf.py", "requirements.txt"}:
                p.unlink()
        shutil.rmtree(str(path / "tests"))
        # download license
        license_text = self.parser.download_license_template(header=False)
        Path(path / "LICENSE.txt").write_text(license_text, encoding="utf8")
        # copy resources, overwriting
        for source in (path / "tyrannosaurus" / "resources").iterdir():
            if not Path(source).is_file():
                continue
            resource = Path(source).name
            # $dot so we can circumvent the .gitignore
            resource = resource.replace("$dot", ".")
            resource = resource.replace("$project", self.project_name)
            resource = resource.replace("$pkg", self.pkg_name)
            # Remove .{other-extension}.txt at the end, with some restrictions
            # Don't fix, e.g. beautiful.butterfly.txt
            # But do replace .json.txt
            # Our ad-hoc rule is that an "extension" contains between 1 and 5 characters
            # (Also forbid a @ in the extension -- that's a path separator.)
            if resource.endswith(".txt"):
                resource = resource[:-4]
            # TODO: Fix this
            # resource = re.compile(r"^.*?(\.[^.@]{1,5})\.txt$").sub(r"\1", resource)
            dest = path / Path(*resource.split("@"))
            dest.parent.mkdir(parents=True, exist_ok=True)
            text = self.parser.parse(source.read_text(encoding="utf8"))
            # Also replace ${LICENSE.HEADER}
            # This is a special one: We don't currently do this in the context
            dest.write_text(text, encoding="utf8")
        # remove unneeded tyrannosaurus source dir
        # we already copied the files in tyrannosaurus/resources/
        shutil.rmtree(str(path / "tyrannosaurus"))
        # track remote via git
        if self.should_track:
            self._track(path)

    def _track(self, path: Path) -> None:
        is_initialized = self._call(
            ["git", "init", "--initial-branch=main"],
            cwd=path,
            fail="Failed calling git init. Giving up.",
        )
        if is_initialized:
            self._call(
                ["pre-commit", "install"], cwd=path, fail="Failed calling pre-commit install."
            )
            is_tracked = self._call(
                ["git", "remote", "add", "origin", self.repo_to_track],
                cwd=path,
                fail=f"Failed tracking {self.repo_to_track}",
            )
            if is_tracked:
                self._call(
                    ["git", "branch", "--set-upstream-to=origin/main", "main"],
                    cwd=path,
                    fail=f"Failed setting upstream to {self.repo_to_track}",
                )
        logger.info(f"Initialized new git repo tracking remote {self.repo_to_track}")

    def _checkout(self, path: Path) -> None:
        if path.exists():
            raise FileExistsError(f"Path {path} already exists")
        try:
            path.parent.mkdir(exist_ok=True, parents=True)
            logger.info("Running git clone...")
            self._call(["git", "clone", tyranno_url, str(path)])
            # FYI this would fail if we had deleted .git first
            self._set_tyranno_vr(path)
        finally:
            self._murder_evil_path_for_sure(path / ".git")

    def _set_tyranno_vr(self, path: Path):
        # if it's None, just leave it as HEAD
        if self.tyranno_vr == "latest":
            logger.info(f"Using HEAD for tyrannosaurus template version")
        else:
            tyranno_vr = self._parse_tyranno_vr(path, self.tyranno_vr)
            try:
                self._checkout_rev(path, tyranno_vr)
            except VersionNotFoundError:
                # if it was set as 'current', we might have failed because we're testing an unreleased version
                if self.tyranno_vr == "current":
                    logger.warning(
                        f"Installed tyrannosaurus version {tyranno_vr} not found; using stable"
                    )
                    tyranno_vr = self._parse_tyranno_vr(path, "stable")
                    self._checkout_rev(path, tyranno_vr)
                    # if that still doesn't work, let it fail
                else:
                    # let everything else fail, including for "stable"
                    raise
            logger.info(f"Using tyrannosaurus template version {tyranno_vr}")

    def _checkout_rev(self, path: Path, tyranno_vr: str):
        self._call(
            ["git", "checkout", f"tags/{tyranno_vr}".strip()],
            cwd=path,
            fail=VersionNotFoundError(f"Git tag '{tyranno_vr}' was not found."),
        )

    def _parse_tyranno_vr(self, path: Path, version: str) -> Optional[str]:
        version = version.lower().strip()
        if version == "latest":
            return None
        elif version == "current":
            from tyrannosaurus import TyrannoInfo

            return "v" + TyrannoInfo.version
        elif version == "stable":
            return self._call(["git", "describe", "--abbrev=0", "--tags"], cwd=path)
        elif version.startswith("v"):
            return version
        return "v" + version

    def _call(
        self,
        cmd: List[str],
        cwd: Optional[Path] = None,
        succeed: Optional[str] = None,
        fail: Union[None, str, BaseException] = None,
    ) -> Optional[str]:
        kwargs: Dict[str, str] = {} if cwd is None else dict(cwd=str(cwd))
        if not self.debug:
            kwargs["stderr"] = PIPE
        try:
            output = check_output(cmd, encoding="utf8", **kwargs)  # nosec
        except CalledProcessError:
            logger.debug(f"Failed calling {' '.join(cmd)} in {cwd}", exc_info=True)
            if fail is not None and isinstance(fail, BaseException):
                raise fail
            elif fail is not None:
                logger.error(fail)
            return None
        else:
            logger.debug(f"Succeeded calling {' '.join(cmd)} in {cwd}", exc_info=True)
            if succeed is not None:
                logger.info(succeed)
            return output

    def _murder_evil_path_for_sure(self, evil_path: Path) -> None:
        """
        There are likely to be permission issues with .git directories.

        Args:
            evil_path: The .git directory
        """
        try:
            shutil.rmtree(str(evil_path))
        except OSError:
            logger.debug("Could not delete .git with rmtree", exc_info=True)

            def on_rm_error(func, path, exc_info):
                # from: https://stackoverflow.com/questions/4829043/how-to-remove-read-only-attrib-directory-with-python-in-windows
                os.chmod(path, stat.S_IWRITE)
                os.unlink(path)

            shutil.rmtree(str(evil_path), onerror=on_rm_error)


__all__ = ["New"]
