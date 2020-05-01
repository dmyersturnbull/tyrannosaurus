# Tyrannosaurus Reqs

[![Build status](https://img.shields.io/pypi/status/tyrannosaurus)](https://pypi.org/project/tyrannosaurus/)
[![Latest version on PyPi](https://badge.fury.io/py/tyrannosaurus.svg)](https://pypi.org/project/tyrannosaurus/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/tyrannosaurus.svg)](https://pypi.org/project/tyrannosaurus/)
[![Documentation status](https://readthedocs.org/projects/tyrannosaurus/badge/?version=latest&style=flat-square)](https://readthedocs.org/projects/tyrannosaurus/)
[![Travis](https://travis-ci.org/dmyersturnbull/tyrannosaurus.svg?branch=master)](https://travis-ci.org/dmyersturnbull/tyrannosaurus)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

An opinionated 2020 Python template.
Just clone it and modify or run `tyrannosaurus new`.

⚠ Status: Under development

Provides `tyrannosaurus sync` to copy metadata from your `pyproject.toml` other config files,
including `tox.ini`, `.flake8`, `docs/conf.py`, `docs/requirements.txt`, `LICENSE.txt`, and `recipes/.../meta.yaml`.
You can configure this in a `tool.tyrannosaurus` section of `pyproject.toml`.
For an example, see [tyrannosaurus's own pyproject.toml](https://github.com/dmyersturnbull/tyrannosaurus/blob/master/pyproject.toml) file.

The information copied includes version, description, dependencies, and preferred line length.
Always generates backups under `.tyrannosaurus` before modifying.
You can clear this and other temp files with `tyrannosaurus clean`.

Projects are configured for:
- Build: Poetry, Tox, Conda, DepHell, Travis
- Style: Black, Coverage, MyPy, Flake8, pycodestyle, pydocstyle, EditorConfig, pre-commit-hooks
- Documentation: ReadTheDocs, Sphinx, Napoleon, autodoc, viewcode
- Deploy: wheels, sdist, Twine, Docker, Conda-Forge

[Poetry](https://github.com/python-poetry/poetry) is fantastic and highly recommended.
Also see [DepHell](https://github.com/dephell/dephell) and [conda-forge](https://conda-forge.org/).

### Building, extending, and contributing

[New issues](https://github.com/dmyersturnbull/tyrannosaurus/issues) and pull requests are welcome.

Tyrannosaurus is licensed under the [Apache License, version 2.0](https://www.apache.org/licenses/LICENSE-2.0).
The author wrote it after making 18 Git commits trying to configure readthedocs, PyPi, and Tox.
This avoids that struggle for 99% of projects.

Conda build:
1. `pip install m2-patch`
2. `conda skeleton pypi tyrannosaurus`


```
                                              .++++++++++++.
                                           .++HHHHHHH^^HHH+.
                                          .HHHHHHHHHH++-+-++.
                                         .HHHHHHHHHHH:t~~~~~
                                        .+HHHHHHHHHHjjjjjjjj.
                                       .+NNNNNNNNN/++/:--..
                              ........+NNNNNNNNNN.
                          .++++BBBBBBBBBBBBBBB.
 .tttttttt:..           .++BBBBBBBBBBBBBBBBBBB.
+tt+.      ``         .+BBBBBBBBBBBBBBBBBBBBB+++cccc.
ttt.               .-++BBBBBBBBBBBBBBBBBBBBBB++.ccc.
+ttt++++:::::++++++BBBBBBBBBBBBBBBBBBBBBBB+..++.
.+TTTTTTTTTTTTTBBBBBBBBBBBBBBBBBBBBBBBBB+.    .ccc.
  .++TTTTTTTTTTBBBBBBBBBBBBBBBBBBBBBBBB+.      .cc.
    ..:++++++++++++++++++BBBBBB++++BBBB.
           .......      -LLLLL+. -LLLLL.
                        -LLLL+.   -LLLL+.
                        +LLL+       +LLL+
                        +LL+         +ff+
                        +ff++         +++:
                        ++++:
```
