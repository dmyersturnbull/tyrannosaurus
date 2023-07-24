# SPDX-License-Identifier: Apache-2.0
# Source: https://github.com/dmyersturnbull/tyranno
"""
'clean' command for Tyranno.
"""
import shutil
from collections.abc import Generator
from dataclasses import dataclass
from pathlib import Path

from tyranno.model.context import Context

__all__ = ["Clean"]


@dataclass(frozen=True)
class Clean:
    context: Context
    trash_patterns: list[str]
    dry_run: bool

    def run(self) -> Generator[Path, None, None]:
        for path in self._find():
            self._trash(path)
            yield path

    def _find(self) -> Generator[Path, None, None]:
        for pat in self.trash_patterns:
            for path in self.context.repo_path.glob(pat):
                yield path

    def _trash(self, source: Path) -> None:
        dest = self.context.repo_path / source
        if not self.dry_run:
            dest.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(str(source), str(dest))
