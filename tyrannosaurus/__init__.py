"""
Metadata for Tyrannosaurus.
"""

from pathlib import Path, PurePath
from typing import Union

# importlib.metadata is compat with Python 3.8 only
from importlib_metadata import metadata as __load

metadata = __load(Path(__file__).parent.name)
__status__ = "Development"
__copyright__ = "Copyright 2020"
__date__ = "2020-05-15"
__uri__ = metadata["home-page"]
__title__ = metadata["name"]
__summary__ = metadata["summary"]
__license__ = metadata["license"]
__version__ = metadata["version"]
__author__ = metadata["author"]
__maintainer__ = metadata["maintainer"]
__contact__ = metadata["maintainer"]


def resource(*nodes: Union[PurePath, str]) -> Path:
    """Gets a path of a resource file under resources/ directory."""
    return Path(Path(__file__).parent, "resources", *nodes)
