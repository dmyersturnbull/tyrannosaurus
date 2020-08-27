"""
Sync tool.
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Mapping, Sequence

from tyrannosaurus.context import _Context

logger = logging.getLogger(__package__)


class Sync:
    def __init__(self, context: _Context):
        self.context = context

    def sync(self) -> Sequence[str]:  # pragma: no cover
        self.fix_init()
        self.fix_recipe()
        return [str(s) for s in self.context.targets]

    def has(self, key: str):
        return self.context.has_target(key)

    def fix_init(self) -> Sequence[str]:  # pragma: no cover
        if self.has("init"):
            return self.fix_init_internal(self.context.path / self.context.project / "__init__.py")
        return []

    def fix_init_internal(self, init_path: Path) -> Sequence[str]:
        return self.replace_substrs(
            init_path,
            {
                "__status__ = ": f'__status__ = "{self.context.source("status")}"',
                "__copyright__ = ": f'__copyright__ = "{self.context.source("copyright")}"',
                "__date__ = ": f'__date__ = "{self.context.source("date")}"',
            },
        )

    def fix_recipe(self) -> Sequence[str]:  # pragma: no cover
        if self.has("recipe"):
            return self.fix_recipe_internal(self.context.path_source("recipe"))
        return []

    def fix_recipe_internal(self, recipe_path: Path) -> Sequence[str]:
        return self.replace_substrs(
            recipe_path,
            {"{% set version = ": '{% set version = "' + str(self.context.version) + '" %}'},
        )

    def replace_substrs(self, path: Path, replace: Mapping[str, str]) -> Sequence[str]:
        if not self.context.dry_run:
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
        if not self.context.dry_run:
            path.write_text(new_lines, encoding="utf8")
        logger.debug(f"Wrote to {path}")
        return new_lines.splitlines()


__all__ = ["Sync"]
