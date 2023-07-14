# SPDX-License-Identifier Apache-2.0
# Source: https://github.com/dmyersturnbull/tyranno
"""
'update' command for Tyranno.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Mapping


class Update:
    def __init__(self, context: Context):
        self.context = context

    def update(self) -> tuple[Mapping[str, tuple[str, str]], Mapping[str, tuple[str, str]]]:
        helper = PyPiHelper()
        updates = helper.new_versions(self.context.deps)
        dev_updates = helper.new_versions(self.context.dev_deps)
        return updates, dev_updates


__all__ = ["Update"]
