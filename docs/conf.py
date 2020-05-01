"""
Sphinx config file for Tyrannosaurus.

Uses several extensions to get API docs and sourcecode.
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# -- Docs setup --------------------------------------------------------------
# Sphinx recommends adding modules for autodoc this way:
# fmt: off
import sys
from pathlib import Path

root = Path(__file__).parent.parent.absolute()
sys.path.insert(0, str(root))
from tyrannosaurus import __author__, __copyright__, __title__, __version__
# fmt:on

extensions = ["autoapi.extension", "sphinx.ext.napoleon", "sphinx_rtd_theme"]
autoapi_type = "python"
autoapi_dirs = [str(root / __title__)]
master_doc = "index"

# -- Project information -----------------------------------------------------

project = __title__
copyright = __copyright__
author = __author__
version = __version__
release = __version__
language = None

# -- General configuration ---------------------------------------------------
exclude_patterns = ["_build", "Thumbs.db", ".*", "~*", "*~", "*#"]
html_theme = "sphinx_rtd_theme"
