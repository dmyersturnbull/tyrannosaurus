# Tyrannosaurus Reqs

[![Docker](https://img.shields.io/docker/v/dmyersturnbull/tyrannosaurus)](https://hub.docker.com/repository/docker/dmyersturnbull/tyrannosaurus)
[![Latest version on PyPi](https://badge.fury.io/py/tyrannosaurus.svg)](https://pypi.org/project/tyrannosaurus/)
[![Documentation status](https://readthedocs.org/projects/tyrannosaurus/badge/?version=latest&style=flat-square)](https://tyrannosaurus.readthedocs.io/en/stable/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Build status](https://img.shields.io/pypi/status/tyrannosaurus)](https://pypi.org/project/tyrannosaurus/)
[![Build & test](https://github.com/dmyersturnbull/tyrannosaurus/workflows/Build%20&%20test/badge.svg)](https://github.com/dmyersturnbull/tyrannosaurus/actions)
[![Travis](https://travis-ci.org/dmyersturnbull/tyrannosaurus.svg?branch=master)](https://travis-ci.org/dmyersturnbull/tyrannosaurus)

An opinionated Python template for 2020.
No setup.py, requirements.txt, or eggs.

I wrote this after making nearly 50 commits to configure
readthedocs, PyPi, Tox, Docker, Travis, and Github actions.
This avoids that struggle for 99% of projects.
Just clone and modify or use `tyrannosaurus new`.
Install with `pip install tyrannosaurus`.

- _When you commit_, your code will be linted.
- _When you push or make a pull request_, your code will be built and tested.
  Metadata will be synced, security checks will be run, style will be checked,
  documentation will be generated, and docker images, sdists, and wheels will be built.
- _When you release on Github_, your code will be published on PyPi.
  Just add `PYPI_TOKEN` as a Github repo secret.

⚠ Status: Alpha. Generally works pretty well, but
   the `sync` command does less than advertised.

##### Integrations:

Also comes with nice Github labels, issue templates, a changelog template,
Travis support, Conda recipe and environment generation, and other integrations.
Tyrannosaurus itself is included as a dependency.
It will clean up unwanted files and sync metadata from `pyproject.toml` to other files,
such as Anaconda recipes and environment files, license headers, doc and tox requirements, and author/contributor lists.
Target files can be disabled in `[tool.tyrannosaurus.targets]`.


##### To run:

To run locally, install [Poetry](https://github.com/python-poetry/poetry)
and [Tox](https://tox.readthedocs.io/en/latest/) (`pip install tox`).
Then just type `tox` to build artifacts and run tests.
To create an initial Anaconda recipe or environment file, run `tyrannosaurus recipe` or `tyrannosaurus env`.

[See the docs](https://tyrannosaurus.readthedocs.io/en/stable/) for more information.

##### Contributing:

[New issues](https://github.com/dmyersturnbull/tyrannosaurus/issues) and pull requests are welcome.
Please refer to the [contributing guide](https://github.com/dmyersturnbull/tyrannosaurus/blob/master/CONTRIBUTING.md).


```text
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
