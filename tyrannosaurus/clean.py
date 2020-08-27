"""
Tyrannosaurus command-line interface.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional, Sequence
from typing import Tuple as Tup

from tyrannosaurus.context import _Context
from tyrannosaurus.helpers import _fast_scandir, _TrashList

logger = logging.getLogger(__package__)


class Clean:
    def __init__(self, dists: bool, aggressive: bool, hard_delete: bool, dry_run: bool):
        self.dists = dists
        self.aggressive = aggressive
        self.hard_delete = hard_delete
        self.dry_run = dry_run

    def clean(self, path: Path) -> Sequence[Tup[Path, Optional[Path]]]:
        context = _Context(path, dry_run=self.dry_run)
        logger.info(f"Clearing {context.tmp_path}")
        trashed = []
        destroyed = context.destroy_tmp()
        if destroyed:
            trashed.append((context.tmp_path, None))
        trash = _TrashList(self.dists, self.aggressive)
        # we're going to do these in order to save time overall
        for p in trash.get_list():
            tup = context.trash(p, self.hard_delete)
            if tup[0] is not None:
                trashed.append(tup)
        for p in _fast_scandir(path, trash):
            if trash.should_delete(p):
                tup = context.trash(p, self.hard_delete)
                if tup[0] is not None:
                    trashed.append(tup)
        return trashed


__all__ = ["Clean"]
