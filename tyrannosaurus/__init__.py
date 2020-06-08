"""
Metadata for this project.
"""

import logging
from pathlib import Path, PurePath
from typing import Union

# importlib.metadata is compat with Python 3.8 only
from importlib_metadata import PackageNotFoundError, metadata as __load

logger = logging.getLogger(Path(__file__).parent.name)

metadata = None
try:
    metadata = __load(Path(__file__).absolute().parent.name)
    __status__ = "Development"
    __copyright__ = "Copyright 2020"
    __date__ = "2020-06-08"
    __uri__ = metadata["home-page"]
    __title__ = metadata["name"]
    __summary__ = metadata["summary"]
    __license__ = metadata["license"]
    __version__ = metadata["version"]
    __author__ = metadata["author"]
    __maintainer__ = metadata["maintainer"]
    __contact__ = metadata["maintainer"]
except PackageNotFoundError:
    logger.error(
        "Could not load package metadata for {}. Is it installed?".format(
            Path(__file__).absolute().parent.name
        )
    )


def resource(*nodes: Union[PurePath, str]) -> Path:
    """Gets a path of a resource file under resources/ directory."""
    return Path(Path(__file__).parent, "resources", *nodes)


if __name__ == "__main__":
    if metadata is not None:
        print("{} (v{})".format(metadata["name"], metadata["version"]))
    else:
        print("Unknown project info")
