"""
Anaconda environments.

Original source: https://github.com/dmyersturnbull/tyrannosaurus
Copyright 2020–2021 Douglas Myers-Turnbull
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0
"""
import logging
from pathlib import Path
from typing import Sequence

from tyrannosaurus.context import Context
from tyrannosaurus.helpers import EnvHelper


logger = logging.getLogger(__package__)


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


__all__ = ["CondaEnv"]
