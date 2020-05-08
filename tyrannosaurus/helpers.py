"""
Support code for Tyrannosaurus.
"""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Sequence, Mapping

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


__all__ = ["_TrashList", "_SyncHelper"]
