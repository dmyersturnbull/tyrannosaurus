"""
Original source: https://github.com/dmyersturnbull/tyrannosaurus
Copyright 2020–2021 Douglas Myers-Turnbull
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0
Module that cleans up temporary files.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional, Sequence
from typing import Tuple as Tup

from tyrannosaurus.context import Context
from tyrannosaurus.helpers import TrashList, scandir_fast

logger = logging.getLogger(__package__)


class Clean:
    def __init__(self, dists: bool, aggressive: bool, hard_delete: bool, dry_run: bool):
        self.dists = dists
        self.aggressive = aggressive
        self.hard_delete = hard_delete
        self.dry_run = dry_run

    def clean(self, path: Path) -> Sequence[Tup[Path, Optional[Path]]]:
        context = Context(path, dry_run=self.dry_run)
        logger.info(f"Clearing {context.tmp_path}")
        trashed = []
        destroyed = context.destroy_tmp()
        if destroyed:
            trashed.append((context.tmp_path, None))
        trash = TrashList(self.dists, self.aggressive)
        # we're going to do these in order to save time overall
        for p in trash.get_list():
            tup = context.trash(p, self.hard_delete)
            if tup[0] is not None:
                trashed.append(tup)
        for p in scandir_fast(path, trash):
            p = Path(p)
            if trash.should_delete(p):
                tup = context.trash(p, self.hard_delete)
                if tup[0] is not None:
                    trashed.append(tup)
        return trashed


__all__ = ["Clean"]
