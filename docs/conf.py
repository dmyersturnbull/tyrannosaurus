# Config file for Sphinx
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Docs setup --------------------------------------------------------------
# Sphinx recommends adding modules for autodoc this way:
import sys
from pathlib import Path
root = Path(__file__).parent.parent.absolute()
sys.path.insert(0, str(root))
print(sys.path)
extensions = ['sphinx.ext.autodoc', 'autoapi.sphinx', 'sphinx.ext.napoleon', 'sphinx.ext.viewcode']
autoapi_type = 'python'
autoapi_dirs = [str(root/'tyrannosaurus')]

# -- Project information -----------------------------------------------------
from tyrannosaurus import ProjectInfo as X
project = X.name
copyright = X.copyright
author = X.author
version = X.version
release = X.release
language = 'en'

# -- General configuration ---------------------------------------------------
exclude_patterns = ['_build', 'Thumbs.db', '.*', '~*', '*~', '*#']
html_theme = 'alabaster'
