"""
Sphinx config file.

Uses several extensions to get API docs and sourcecode.
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

from pathlib import Path

import tomlkit

root = Path(__file__).parent.parent.absolute()
toml = tomlkit.loads((root / "pyproject.toml").read_text(encoding="utf8"))


def find(key: str) -> str:
    return str(toml["tool"]["poetry"][key])


language = None
project = find("name")
version = find("version")
release = find("version")
author = ", ".join(find("authors"))
copyright = "Copyright (2016)"


extensions = ["autoapi.extension", "sphinx.ext.napoleon", "sphinx_rtd_theme"]
autoapi_type = "python"
autoapi_dirs = [str(root / project)]
master_doc = "index"
napoleon_include_special_with_doc = True
autoapi_keep_files = True
autoapi_python_class_content = "both"
autoapi_options = ["private-members=false"]


exclude_patterns = ["_build", "Thumbs.db", ".*", "~*", "*~", "*#"]
html_theme = "sphinx_rtd_theme"
