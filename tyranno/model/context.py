# SPDX-License-Identifier Apache-2.0
# Source: https://github.com/dmyersturnbull/tyranno
"""
Wrapper around repo for Tyranno.
"""
import re
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path, PurePath
from typing import Self

import jmespath
import platformdirs

from tyranno.model._wrapped_toml import TomlBranch, TomlLeaf, WrappedToml

pattern = re.compile(r"\$\{ *([-._A-Za-z0-9]*) *(?:~ *([^~]+) *~ *)?\}")


@dataclass(frozen=True)
class Context:
    repo_path: Path
    temp_path: Path
    data: WrappedToml

    @classmethod
    def of(cls) -> Self:
        return cls()  # TODO

    @property
    def trash_path(self) -> Path:
        return self.repo_path / ".#trash"

    @property
    def config_path(self) -> Path:
        return platformdirs.user_config_path("tyranno")

    @property
    def cache_path(self) -> Path:
        return platformdirs.user_cache_path("tyranno")

    def resolve_path(self, path: PurePath | str) -> Path:
        path = Path(path)
        path = path.resolve(strict=True)
        if not str(path).startswith(str(self.repo_path)):
            raise ValueError(f"{path} is not a descendent of {self.repo_path}")
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
                result = pattern.sub(lambda p: self._sub(p.group(1), p.group(2)), value)
            case int() | float() | datetime() | date():
                result = value
            case _:
                raise AssertionError(f"Impossible type {value}")
        return jmespath.search(james, result) if james else result


__all__ = ["Context"]
