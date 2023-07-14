"""
Sphinx config file.

Uses several extensions to get API docs and sourcecode.
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import tomllib as toml
from pathlib import Path
from typing import TypeVar

# This assumes that we have the full project root above, containing pyproject.toml
_root = Path(__file__).parent.parent.absolute()
_toml = toml.loads((_root / "pyproject.toml").read_text(encoding="utf8"))

T = TypeVar("T")


def find(key: str, default: T | None = None, as_type: type[T] = str) -> T | None:
    """
    Gets a value from pyproject.toml, or a default.

    Args:
        key: A period-delimited TOML key; e.g. ``tools.poetry.name``
        default: Default value if any node in the key is not found
        as_type: Convert non-``None`` values to this type before returning

    Returns:
        The value converted to ``as_type``, or ``default`` if it was not found
    """
    at = _toml
    for k in key.split("."):
        at = at.get(k)
        if at is None:
            return default
    return as_type(at)


# Basic information, used by Sphinx
# Leave language as None unless you have multiple translations
language = None
project = find("tool.poetry.name")
version = find("tool.poetry.version")
release = version
author = ", ".join(find("tool.poetry.authors", as_type=list))

# Copyright string (for documentation)
# It's not clear whether we're supposed to, but we'll add the license
# noinspection PyShadowingBuiltins
copyright = find("tool.tyranno.data.copyright")
_license = find("tool.tyranno.data.doc_license")
_license_url = find("tool.tyranno.data.doc_license_url")

# Load extensions
# These should be in docs/requirements.txt
# Napoleon is bundled in Sphinx, so we don't need to list it there
# NOTE: 'autoapi' here refers to sphinx-autoapi
# See https://sphinx-autoapi.readthedocs.io/
extensions = [
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
]
master_doc = "index"
napoleon_include_special_with_doc = True
autoapi_type = "python"
autoapi_dirs = [str(_root / project)]
autoapi_keep_files = True
autoapi_python_class_content = "both"
autoapi_member_order = "groupwise"
autoapi_options = ["private-members", "undoc-members", "special-members"]

# The vast majority of Sphinx themes are unmaintained
# This includes alabaster and readthedocs
# Furo is well-maintained as of 2023
# These can be specific to the theme, or processed by Sphinx directly
# https://www.sphinx-doc.org/en/master/usage/configuration.html
html_theme = "furo"

# doc types to build
sphinx_enable_epub_build = False
sphinx_enable_pdf_build = False
exclude_patterns = ["_build", "Thumbs.db", ".*", "~*", "*~", "*#"]
