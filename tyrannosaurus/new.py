from __future__ import annotations

import logging
import os
import shutil
import stat
from pathlib import Path
from subprocess import CalledProcessError, check_call
from typing import Sequence, Union

import typer

from tyrannosaurus import __version__ as tyranno_version
from tyrannosaurus.context import _LiteralParser
from tyrannosaurus.helpers import _License

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
        license_name: Union[str, _License],
        username: str,
        authors: Sequence[str],
        description: str,
        keywords: Sequence[str],
        version: str,
        newest: bool,
    ):
        if isinstance(license_name, str):
            license_name = _License[license_name.lower()]
        self.project_name = name.lower()
        self.pkg_name = name.replace("_", "").replace("-", "").replace(".", "").lower()
        self.license_name = license_name
        self.username = username
        self.authors = authors
        self.description = description
        self.keywords = keywords
        self.version = version
        self.newest = newest

    def create(self, path: Path) -> None:
        self._checkout(Path(str(path).lower()))
        logger.info("Got git checkout. Fixing...")
        # remove tyrannosaurus-specific files
        Path(path / "poetry.lock").unlink()
        Path(path / "recipes" / "tyrannosaurus" / "meta.yaml").unlink()
        Path(path / "recipes" / "tyrannosaurus").rmdir()
        for p in Path(path / "docs").iterdir():
            if p.is_file() and p.name not in {"conf.py", "requirements.txt"}:
                p.unlink()
        shutil.rmtree(str(path / "tests" / "resources"))
        for p in Path(path / "tests").iterdir():
            if p.is_file() and p.name != "__init__.py":
                p.unlink()
        # copy license
        parser = _LiteralParser(
            self.project_name,
            self.username,
            self.authors,
            self.description,
            self.keywords,
            self.version,
            self.license_name.name,
        )
        license_file = (
            path / "tyrannosaurus" / "resources" / ("license_" + self.license_name.name + ".txt")
        )
        if license_file.exists():
            text = parser.parse(license_file.read_text(encoding="utf8"))
            Path(path / "LICENSE.txt").write_text(text, encoding="utf8")
        else:
            logger.error(f"License file for {license_file.name} not found")
        # copy resources, overwriting
        for source in (path / "tyrannosaurus" / "resources").iterdir():
            if not Path(source).is_file():
                continue
            resource = Path(source).name
            if not resource.startswith("license_"):
                # TODO replace project with pkg
                resource = (
                    str(resource)
                    .replace(".py.txt", ".py")
                    .replace(".toml.txt", ".toml")
                    .replace("$project", self.project_name)
                    .replace("$pkg", self.pkg_name)
                )
                dest = path / Path(*resource.split("@"))
                if dest.name.startswith("-"):
                    dest = Path(*reversed(dest.parents), "." + dest.name[1:],)
                dest.parent.mkdir(parents=True, exist_ok=True)
                text = parser.parse(source.read_text(encoding="utf8"))
                dest.write_text(text, encoding="utf8")
        # rename some files
        Path(path / self.pkg_name).mkdir(exist_ok=True)
        Path(path / "recipes" / self.pkg_name).mkdir(parents=True)
        (path / "tyrannosaurus" / "__init__.py").rename(Path(path / self.pkg_name / "__init__.py"))
        shutil.rmtree(str(path / "tyrannosaurus"))

    def _checkout(self, path: Path):
        if path.exists():
            raise FileExistsError(f"Path {path} already exists")
        path.parent.mkdir(exist_ok=True, parents=True)
        logger.info("Running git clone...")
        check_call(
            ["git", "clone", "https://github.com/dmyersturnbull/tyrannosaurus.git", str(path)]
        )
        if not self.newest:
            try:
                check_call(["git", "checkout", f"tags/v{tyranno_version}"], cwd=str(path))
            except CalledProcessError:
                raise VersionNotFoundError(f"Git tag 'v{tyranno_version}' was not found.")
        self._murder_evil_path_for_sure(path / ".git")

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
