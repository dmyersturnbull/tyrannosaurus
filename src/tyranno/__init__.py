# SPDX-License-Identifier: Apache-2.0
# Source: https://github.com/dmyersturnbull/tyranno
"""
Metadata for Tyranno.
"""
import logging
from datetime import UTC, datetime
from importlib.metadata import PackageNotFoundError
from importlib.metadata import metadata as __load
from pathlib import Path

import platformdirs

TYRANNO_CACHE = platformdirs.user_cache_path("tyranno")
TYRANNO_CONFIG = platformdirs.user_cache_path("tyranno")

pkg = Path(__file__).parent.name
logger = logging.getLogger(pkg)
metadata = None
try:
    metadata = __load(pkg)
except PackageNotFoundError:  # pragma: no cover
    logger.error(f"Could not load package metadata for {pkg}. Is it installed?")
    __uri__ = None
    __title__ = None
    __summary__ = None
    __version__ = None
else:
    __uri__ = metadata["home-page"]
    __title__ = metadata["name"]
    __summary__ = metadata["summary"]
    __version__ = metadata["version"]


class ProjectInfo:
    version = __version__
    now_utc = datetime.now(UTC)
    now_local = now_utc.astimezone()
