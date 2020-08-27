"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Mapping
from typing import Tuple as Tup

import typer

from tyrannosaurus.context import _Context
from tyrannosaurus.helpers import _PyPiHelper

logger = logging.getLogger(__package__)
cli = typer.Typer()


class Update:
    def __init__(self, dry_run: bool):
        self.dry_run = dry_run

    def update(self, path: Path) -> Tup[Mapping[str, Tup[str, str]], Mapping[str, Tup[str, str]]]:
        context = _Context(path, dry_run=self.dry_run)
        helper = _PyPiHelper()
        updates = helper.new_versions(context.deps)
        dev_updates = helper.new_versions(context.dev_deps)
        return updates, dev_updates

__all__ = ["Update"]
"""
