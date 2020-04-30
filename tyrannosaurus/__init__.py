# importlib.metadata is compat with Python 3.8 only
from importlib_metadata import metadata as __load

metadata = __load("tyrannosaurus")
__license__ = metadata["license"]
__version__ = metadata["version"]
