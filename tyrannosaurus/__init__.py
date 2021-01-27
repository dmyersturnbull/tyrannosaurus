"""
Original source: https://github.com/dmyersturnbull/tyrannosaurus
Copyright 2020–2021 Douglas Myers-Turnbull
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0

Metadata for Tyrannosaurus.
"""
import logging

from datetime import datetime, timezone
from importlib.metadata import PackageNotFoundError
from importlib.metadata import metadata as __load
from pathlib import Path


pkg = Path(__file__).absolute().parent.name
logger = logging.getLogger(pkg)
metadata = None
try:
    metadata = __load(pkg)
    __status__ = "Development"
    __copyright__ = "Copyright 2020–2021"
    __date__ = "2020-09-25"
    __uri__ = metadata["home-page"]
    __title__ = metadata["name"]
    __summary__ = metadata["summary"]
    __license__ = metadata["license"]
    __version__ = metadata["version"]
    __author__ = metadata["author"]
    __maintainer__ = metadata["maintainer"]
    __contact__ = metadata["maintainer"]
except PackageNotFoundError:  # pragma: no cover
    logger.error(f"Could not load package metadata for {pkg}. Is it installed?")


class TyrannoInfo:
    copyright = __copyright__
    version = __version__
    now_utc = datetime.now(timezone.utc)
    now = now_utc.astimezone()
    today = now.date()
    datestamp = now.strftime("%Y-%m-%d")
    timestamp = now.strftime("%Y-%m-%dT%H-%M-%S")
    pretty_timestamp_utc = (
        now_utc.replace(microsecond=0).isoformat().replace("T", " ").replace("+00:00", " Z")
    )
    pretty_timestamp_with_offset = now.strftime("%Y-%m-%d %H-%M-%S") + " " + now.isoformat()[-6:]


if __name__ == "__main__":  # pragma: no cover
    if metadata is not None:
        print(f"{pkg} (v{metadata['version']})")
    else:
        print(f"Unknown project info for {pkg}")
