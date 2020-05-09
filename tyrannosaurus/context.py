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
        assert isinstance(items, str), "Failed with '{}'".format(items)
        if "." not in items:
            return self.x[items]
        at = self.x
        for item in items.split("."):
            at = at[item]
        if isinstance(at, dict):
            return _Toml(at)
        return at

    def __contains__(self, items):
        assert isinstance(items, str), "Failed with '{}'".format(items)
        if "." not in items:
            return items in self.x
        at = self.x
        for item in items.split("."):
            if item not in at:
                return False
            at = at[item]
        return True

    def items(self):
        return self.x.items()

    def keys(self):
        return self.x.keys()

    def __str__(self):
        return self.__class__.__name__ + "(" + repr(self.x) + ")"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.x) + ")"

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
        self, project: str, version: str, user: Optional[str], authors: Optional[Sequence[str]]
    ):
        self.project = project
        self.version = version
        self.user = user
        self.authors = authors

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
            .replace("${project}", self.project)
            .replace("${version}", self.version)
        )
        if self.user is not None:
            s = s.replace("${user}", self.user)
        if self.authors is not None:
            s = s.replace("${authors}", ",".join(self.authors))
        return s


class _Source:
    @classmethod
    def parse(cls, s: str, toml: _Toml) -> str:
        project = toml["tool.poetry.name"]
        version = toml["tool.poetry.version"]
        if s.startswith("'") and s.endswith("'"):
            return _LiteralParser(project, version, None, None).parse(s).strip("'")
        else:
            value = toml[s]
            return str(value)


class _Context:
    def __init__(
        self, path: Union[Path, str] = Path(os.getcwd()), data=None, dry_run: bool = False
    ):
        self.path = Path(path).resolve()
        if data is None:
            data = _Toml.read(Path(self.path) / "pyproject.toml")
        self.data = data
        self.options = {k for k, v in data["tool.tyrannosaurus.options"].items() if v}
        self.targets = {k for k, v in data["tool.tyrannosaurus.targets"].items() if v}
        self.sources = {
            k: _Source.parse(v, data) for k, v in data["tool.tyrannosaurus.sources"].items() if v
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
            logger.debug("Generated backup of {} to {}".format(path, bak))

    def trash(
        self, path: Union[Path, str], hard_delete: bool
    ) -> Tup[Optional[Path], Optional[Path]]:
        path = Path(path)
        if not path.exists():
            return None, None
        self.check_path(path)
        if hard_delete:
            if not self.dry_run:
                shutil.rmtree(path)
            logger.debug("Deleted {}".format(path))
            return path, None
        else:
            bak = self.get_bak_path(path)
            bak.parent.mkdir(exist_ok=True, parents=True)
            if not self.dry_run:
                os.rename(str(path), str(bak))
            logger.debug("Trashed {} to {}".format(path, bak))
            return path, bak

    def get_bak_path(self, path: Union[Path, str]):
        if not str(path).startswith(str(self.path)):
            path = self.path / path
        path = Path(path).resolve()
        suffix = path.suffix + "." + timestamp + ".bak"
        return self.tmp_path / path.relative_to(self.path).with_suffix(suffix)

    def check_path(self, path: Union[Path, str]) -> None:
        path = Path(path)
        if path == self.path:
            raise ValueError("Cannot touch {}".format(path))
        if not path.exists():
            raise FileNotFoundError("Path {} does not exist".format(path))
        for parent in path.resolve().parents:
            if parent.resolve() == self.path.resolve():
                return
        raise ValueError("Cannot touch {}".format(path))

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
