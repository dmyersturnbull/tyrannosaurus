"""
Context for Tyrannosaurus.
"""

from __future__ import annotations

import logging
import os
import shutil
from datetime import date, datetime
from pathlib import Path, PurePath
from typing import Any, Mapping, Optional, Sequence
from typing import Tuple as Tup
from typing import Union

import tomlkit

logger = logging.getLogger(__package__)
today = date.today()
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")


class _Toml:
    """A thin wrapper around toml to make getting values easier."""

    @classmethod
    def read(cls, path: Union[PurePath, str]) -> _Toml:
        return _Toml(tomlkit.loads(Path(path).read_text(encoding="utf8")))

    def __init__(self, x: Mapping[str, Any]) -> None:
        self.x = x

    def __getitem__(self, items: str):
        if not isinstance(items, str):
            raise AssertionError(f"Failed with '{items}'")
        if "." not in items:
            return self.x[items]
        at = self.x
        for item in items.split("."):
            at = at[item]
        if isinstance(at, dict):
            return _Toml(at)
        return at

    def __contains__(self, items):
        if not isinstance(items, str):
            raise AssertionError(f"Failed with '{items}'")
        if "." not in items:
            return items in self.x
        at = self.x
        for item in items.split("."):
            if item not in at:
                return False
            at = at[item]
        return True

    def get(self, items: str, default: Any = None) -> Optional[Any]:
        try:
            return self[items]
        except KeyError:
            return default

    def items(self):
        return self.x.items()

    def keys(self):
        return self.x.keys()

    def __str__(self):
        return f"{self.__class__.__name__} ({repr(self.x)})"

    def __repr__(self):
        return f"{self.__class__.__name__} ({repr(self.x)})"

    def __eq__(self, other):
        return isinstance(other, _Toml) and self.x == other.x


class _TomlBuilder:
    def __init__(self):
        self._dict = {}

    def add(self, key: str, value: Any):
        at = self._dict
        if "." in key:
            for k in key.split(".")[:-1]:
                if k not in at:
                    at[k] = {}
                at = at[k]
        at[key.split(".")[-1]] = value
        return self

    def build(self) -> _Toml:
        return _Toml(self._dict)


class _LiteralParser:
    def __init__(
        self,
        project: str,
        user: Optional[str],
        authors: Optional[Sequence[str]],
        description: str,
        keywords: Sequence[str],
        version: str,
        license: str,
    ):
        self.project = project.lower()
        # TODO doing this in two places
        self.pkg = project.replace("_", "").replace("-", "").replace(".", "").lower()
        self.user = user
        self.authors = authors
        self.description = description
        self.keywords = keywords
        self.version = version
        self.license = str(license)
        self.license_official = dict(
            apache2="Apache-2.0",
            cc0="CC0-1.0",
            ccby="CC-BY-4.0",
            ccybync="CC-BY-NC-4.0",
            gpl2="GPL-2.0-or-later",
            gpl3="GPL-3.0-or-later",
            mit="MIT",
        ).get(str(license), "TODO:fix:" + str(license))

    def parse(self, s: str) -> str:
        s = (
            s.replace("${today}", str(today))
            .replace("${today.year}", str(today.year))
            .replace("${today.month}", str(today.month))
            .replace("${today.day}", str(today.day))
            .replace("${now}", timestamp)
            .replace("${now.hour}", str(now.hour))
            .replace("${now.minute}", str(now.minute))
            .replace("${now.second}", str(now.second))
            .replace("${project}", self.project.lower())
            .replace("${Project}", self.project[0].upper() + self.project[1:])
            .replace("${pkg}", self.pkg)
            .replace("${license}", self.license)
            .replace("${license.official}", self.license_official)
            .replace("${version}", self.version)
            .replace("${description}", self.description)
            .replace("${keywords}", str(self.keywords))
        )
        if self.user is not None:
            s = s.replace("${user}", self.user)
        if self.authors is not None:
            s = s.replace("${authors}", str(self.authors))
            s = s.replace("${authors.str}", ", ".join(self.authors))
        return s


class _Source:
    @classmethod
    def parse(cls, s: str, toml: _Toml) -> Union[str, Sequence]:
        project = toml["tool.poetry.name"]
        version = toml["tool.poetry.version"]
        description = toml["tool.poetry.description"]
        authors = toml["tool.poetry.authors"]
        keywords = toml["tool.poetry.keywords"]
        license = toml["tool.poetry.license"]
        if isinstance(s, str) and s.startswith("'") and s.endswith("'"):
            return (
                _LiteralParser(
                    project=project,
                    user=None,
                    authors=authors,
                    description=description,
                    keywords=keywords,
                    version=version,
                    license=license,
                )
                .parse(s)
                .strip("'")
            )
        elif isinstance(s, str):
            value = toml[s]
            return str(value)
        else:
            # TODO not great
            return list(s)


class _Context:
    def __init__(self, path: Union[Path, str], data=None, dry_run: bool = False):
        self.path = Path(path).resolve()
        if data is None:
            data = _Toml.read(Path(self.path) / "pyproject.toml")
        self.data = data
        self.options = {k for k, v in data.get("tool.tyrannosaurus.options", {}).items() if v}
        self.targets = {k for k, v in data.get("tool.tyrannosaurus.targets", {}).items() if v}
        self.sources = {
            k: _Source.parse(v, data)
            for k, v in data.get("tool.tyrannosaurus.sources", {}).items()
            if v
        }
        self.tmp_path = self.path / ".tyrannosaurus"
        self.dry_run = dry_run

    @property
    def project(self) -> str:
        return str(self.data["tool.poetry.name"])

    @property
    def version(self) -> str:
        return str(self.data["tool.poetry.version"])

    @property
    def deps(self) -> Mapping[str, str]:
        return self.data["tool.poetry.dependencies"]

    @property
    def dev_deps(self) -> Mapping[str, str]:
        return self.data["tool.poetry.dev-dependencies"]

    @property
    def extras(self) -> Mapping[str, str]:
        return self.data["tool.poetry.extras"]

    def destroy_tmp(self) -> bool:
        if not self.dry_run:
            if self.tmp_path.exists():
                shutil.rmtree(str(self.tmp_path))
                return True
        return False

    def back_up(self, path: Union[Path, str]) -> None:
        path = Path(path)
        self.check_path(path)
        bak = self.get_bak_path(path)
        if not self.dry_run:
            bak.parent.mkdir(exist_ok=True, parents=True)
            shutil.copyfile(str(path), str(bak))
            logger.debug(f"Generated backup of {path} to {bak}")

    def trash(
        self, path: Union[Path, str], hard_delete: bool
    ) -> Tup[Optional[Path], Optional[Path]]:
        path = Path(path)
        if not path.exists():
            return None, None
        try:
            self.check_path(path)
        except ValueError as e:
            # this can fail while testing
            if path.name == ".pytest_cache":
                logger.debug("Could not deleted .pytest_cache", exc_info=True)
                return path, None
            else:
                raise e
        if hard_delete:
            if not self.dry_run:
                shutil.rmtree(path)
            logger.debug(f"Deleted {path}")
            return path, None
        else:
            bak = self.get_bak_path(path)
            bak.parent.mkdir(exist_ok=True, parents=True)
            if not self.dry_run:
                os.rename(str(path), str(bak))
            logger.debug(f"Trashed {path} to {bak}")
            return path, bak

    def get_bak_path(self, path: Union[Path, str]):
        if not str(path).startswith(str(self.path)):
            path = self.path / path
        path = Path(path).resolve()
        suffix = path.suffix + "." + timestamp + ".bak"
        return self.tmp_path / path.relative_to(self.path).with_suffix(suffix)

    def check_path(self, path: Union[Path, str]) -> None:
        path = Path(path)
        if path.resolve() == self.path.resolve():
            raise ValueError(f"Cannot touch {path}")
        if not path.exists():
            raise FileNotFoundError(f"Path {path} does not exist")
        for parent in path.resolve().parents:
            if parent.resolve() == self.path.resolve():
                return
        raise ValueError(f"Cannot touch {path}")

    def item(self, key: str):
        return self.data[key]

    def poetry(self, key: str):
        return self.data["tool.poetry." + key]

    def has_opt(self, key: str):
        return key in self.options

    def source(self, key: str):
        return self.sources[key]

    def path_source(self, key: str) -> Path:
        output_path = self.path
        for s in str(self.source(key)).split("/"):
            output_path /= s
        return output_path

    def has_target(self, key: str) -> bool:
        return key in self.targets


__all__ = ["_Toml", "_TomlBuilder", "_LiteralParser", "_Context"]
