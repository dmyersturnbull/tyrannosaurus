from __future__ import annotations

import logging
from pathlib import Path
from typing import Sequence

from grayskull.base.factory import GrayskullFactory

from tyrannosaurus.context import _Context
from tyrannosaurus.helpers import _EnvHelper
from tyrannosaurus.sync import Sync

logger = logging.getLogger(__package__)


class Recipe:
    def __init__(self, dry_run: bool):
        self.dry_run = dry_run

    def create(self, context: _Context, output_path: Path) -> Path:
        if output_path.exists():
            context.trash(output_path, False)
        if (output_path / context.project).exists():
            (output_path / context.project).rmdir()
        (output_path / context.project).mkdir(parents=True)
        skull = GrayskullFactory.create_recipe("pypi", context.poetry("name"), "")
        skull.generate_recipe(str(output_path), mantainers=context.source("maintainers").split(","))
        logger.debug("Generated a new recipe at {}".format(output_path))
        helper = Sync(context, self.dry_run)
        helper.fix_recipe()
        logger.debug("Fixed recipe at {}".format(output_path))
        return output_path


class CondaEnv:
    def __init__(self, name: str, dev: bool, extras: bool, dry_run: bool):
        self.name = name
        self.dev = dev
        self.extras = extras
        self.dry_run = dry_run

    def create(self, context: _Context, path: Path):
        deps = self._get_deps(context)
        logger.info("Writing environment with {} dependencies to {} ...".format(len(deps), path))
        lines = _EnvHelper().process(self.name, deps, self.extras)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines), encoding="utf8")

    def _get_deps(self, context: _Context) -> Sequence[str]:
        path = Path(self.name + ".yml")
        if path.exists():
            context.back_up(path)
        deps = dict(context.deps)
        if self.dev:
            deps.update(context.dev_deps)
        return deps


__all__ = ["Recipe", "CondaEnv"]
