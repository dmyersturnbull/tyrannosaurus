"""
Sync tool.
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Sequence, Mapping
from subprocess import check_call

from tyrannosaurus.context import _Context

logger = logging.getLogger(__package__)


class Sync:
    def __init__(self, context: _Context, dry_run: bool):
        self.context = context
        self.dry_run = dry_run

    def sync(self, path: Path) -> Sequence[str]:
        context = _Context(path, dry_run=self.dry_run)
        self.fix_init()
        self.fix_recipe()
        return [str(s) for s in context.targets]

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
                {"{% set version = ": '{% set version = "' + str(self.context.version) + '" %}'},
            )


__all__ = ["Sync"]
