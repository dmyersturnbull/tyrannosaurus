# SPDX-License-Identifier: Apache-2.0
# Source: https://github.com/dmyersturnbull/tyranno
"""
Wrapper around repo for Tyranno.
"""
import os
import re
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path, PurePath
from typing import TYPE_CHECKING, Self

import jmespath
import platformdirs

from tyranno.model._wrapped_toml import TomlBranch, TomlLeaf, WrappedToml

_PATTERN = re.compile(r"\$\{ *([-._A-Za-z0-9]*) *(?:~ *([^~]+) *~ *)?\}")
_TEMP_PATH = os.environ.get("TYRANNO_CACHE_DIR", platformdirs.user_cache_path("tyranno"))
_CONFIG_PATH = os.environ.get("TYRANNO_CONFIG_DIR", platformdirs.user_config_path("tyranno"))


@dataclass(frozen=True, slots=True)
class Context:
    repo_path: Path
    temp_path: Path
    data: WrappedToml

    @classmethod
    def of(cls) -> Self:
        cwd = Path.cwd()
        data = WrappedToml({"project": {"name": cwd.name}})
        for name in (".tyranno.toml", "pyproject.toml"):
            if (cwd / name).exists():
                data = WrappedToml.from_toml_file(cwd / name)
                break
        return cls(
            repo_path=Path.cwd(),
            temp_path=_TEMP_PATH,
            data=data,
        )

    @property
    def trash_path(self) -> Path:
        return self.repo_path / ".#trash"

    @property
    def config_path(self) -> Path:
        return _CONFIG_PATH

    @property
    def cache_path(self) -> Path:
        return _TEMP_PATH

    def resolve_path(self, path: PurePath | str) -> Path:
        path = Path(path)
        path = path.resolve(strict=True)
        if not str(path).startswith(str(self.repo_path)):
            msg = f"{path} is not a descendent of {self.repo_path}"
            raise AssertionError(msg)
        return path.relative_to(self.repo_path)

    def req(self, key: str) -> TomlBranch | TomlLeaf:
        return self._sub(key, None)

    def _sub(self, key: str, james: str | None) -> TomlBranch | TomlLeaf:
        if key == ".":
            key = "tool.tyranno.data"
        elif key.startswith("."):
            key = "tool.tyranno.data" + key
        value = self.data.req(key)
        match value:
            case list():
                result = [self._sub(v, None) for v in value]
            case dict():
                result = {k: self._sub(v, None) for k, v in value.items()}
            case str():
                result = _PATTERN.sub(lambda p: self._sub(p.group(1), p.group(2)), value)
            case int() | float() | datetime() | date():
                result = value
            case _:
                msg = f"Impossible type {value}"
                raise AssertionError(msg)
        return jmespath.search(james, result) if james else result


__all__ = ["Context"]
