"""
Original source: https://github.com/dmyersturnbull/tyrannosaurus
Copyright 2020–2021 Douglas Myers-Turnbull
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

Module that generates Conda recipes and environment files
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional, Sequence

from grayskull.base.factory import GrayskullFactory

from tyrannosaurus.context import Context
from tyrannosaurus.helpers import EnvHelper
from tyrannosaurus.sync import Sync

logger = logging.getLogger(__package__)


class Recipe:
    def __init__(self, context: Context):
        self.context = context

    def create(self, output_dir: Optional[Path]) -> Sequence[str]:
        """
        Creates the recipe file.

        Arguments:

            output_dir: Probably called "recipes"
        """
        context = self.context
        wt = output_dir / context.project
        yaml_path = wt / "meta.yaml"
        if yaml_path.exists():
            context.delete_exact_path(yaml_path, False)
        if wt.exists():
            (output_dir / context.project).rmdir()
        wt.mkdir(parents=True)
        skull = GrayskullFactory.create_recipe("pypi", context.poetry("name"), "")
        skull.generate_recipe(str(output_dir), mantainers=context.source("maintainers").split(","))
        logger.debug(f"Generated a new recipe at {output_dir}/meta.yaml")
        helper = Sync(context)
        lines = helper.fix_recipe_internal(yaml_path)
        logger.debug(f"Fixed recipe at {yaml_path}/meta.yaml")
        return lines


class CondaEnv:
    def __init__(self, name: str, dev: bool, extras: bool):
        self.name = name
        self.dev = dev
        self.extras = extras

    def create(self, context: Context, path: Path) -> Sequence[str]:
        deps = self._get_deps(context)
        logger.info(f"Writing environment with {len(deps)} dependencies to {path} ...")
        lines = EnvHelper().process(self.name, deps, self.extras)
        if not context.dry_run:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("\n".join(lines), encoding="utf8")
        return lines

    def _get_deps(self, context: Context) -> Sequence[str]:
        path = Path(self.name + ".yml")
        if path.exists():
            context.back_up(path)
        deps = dict(context.deps)
        if self.dev:
            deps.update(context.dev_deps)
        return deps


__all__ = ["Recipe", "CondaEnv"]
