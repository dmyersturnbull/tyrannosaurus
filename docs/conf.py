# Config file for Sphinx
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Docs setup --------------------------------------------------------------
# Sphinx recommends adding modules for autodoc this way:
import sys
from pathlib import Path

root = Path(__file__).parent.parent.absolute()
sys.path.insert(0, str(root))
extensions = ["sphinx.ext.autodoc", "autoapi.sphinx", "sphinx.ext.napoleon", "sphinx.ext.viewcode"]
autoapi_type = "python"
autoapi_dirs = [str(root / "tyrannosaurus")]

# -- Project information -----------------------------------------------------
project = "tyrannosaurus"
copyright = "Douglas Myers-Turnbull (2020)"
author = "Douglas Myers-Turnbull"
version = "0.0.5"
release = "0.0.5"
language = "en"

# -- General configuration ---------------------------------------------------
exclude_patterns = ["_build", "Thumbs.db", ".*", "~*", "*~", "*#"]
html_theme = "alabaster"
