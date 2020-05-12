from pathlib import Path, PurePath
from typing import Union


def resource(*nodes: Union[PurePath, str]) -> Path:
    """Gets a path of a test resource file under resources/."""
    return Path(Path(__file__).parent, "resources", *nodes)
