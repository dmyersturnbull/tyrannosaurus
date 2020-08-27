from __future__ import annotations

import logging
from typing import Mapping
from typing import Tuple as Tup

from tyrannosaurus.context import Context
from tyrannosaurus.helpers import PyPiHelper

logger = logging.getLogger(__package__)


class Update:
    def __init__(self, context: Context):
        self.context = context

    def update(self) -> Tup[Mapping[str, Tup[str, str]], Mapping[str, Tup[str, str]]]:
        helper = PyPiHelper()
        updates = helper.new_versions(self.context.deps)
        dev_updates = helper.new_versions(self.context.dev_deps)
        return updates, dev_updates


__all__ = ["Update"]
