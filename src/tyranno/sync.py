# SPDX-License-Identifier: Apache-2.0
# Source: https://github.com/dmyersturnbull/tyranno
"""
'sync' command for Tyranno.
"""
from dataclasses import dataclass

from tyranno.context import Context


@dataclass(frozen=True, slots=True)
class Sync:
    context: Context

    def sync(self) -> None:
        pass


__all__ = ["Sync"]
