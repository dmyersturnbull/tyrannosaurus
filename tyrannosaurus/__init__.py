"""
Metadata for this project.
"""

import logging

# If you need Python < 3.8, change to importlib_metadata and add it as a dependency
from importlib.metadata import PackageNotFoundError
from importlib.metadata import metadata as __load
from pathlib import Path

logger = logging.getLogger(Path(__file__).parent.name)

metadata = None
try:
    metadata = __load(Path(__file__).absolute().parent.name)
    __status__ = "Development"
    __copyright__ = "Copyright 2020"
    __date__ = "2020-06-14"
    __uri__ = metadata["home-page"]
    __title__ = metadata["name"]
    __summary__ = metadata["summary"]
    __license__ = metadata["license"]
    __version__ = metadata["version"]
    __author__ = metadata["author"]
    __maintainer__ = metadata["maintainer"]
    __contact__ = metadata["maintainer"]
except PackageNotFoundError:  # pragma: no cover
    logger.error(
        "Could not load package metadata for {}. Is it installed?".format(
            Path(__file__).absolute().parent.name
        )
    )

if __name__ == "__main__":  # pragma: no cover
    if metadata is not None:
        print("{} (v{})".format(metadata["name"], metadata["version"]))
    else:
        print("Unknown project info")
