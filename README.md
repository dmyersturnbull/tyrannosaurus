# Tyrannosaurus Reqs
[![Version status](https://img.shields.io/pypi/status/tyrannosaurus)](https://pypi.org/project/tyrannosaurus/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tyrannosaurus)](https://pypi.org/project/tyrannosaurus/)
[![Docker](https://img.shields.io/docker/v/dmyersturnbull/tyrannosaurus?color=green&label=DockerHub)](https://hub.docker.com/repository/docker/dmyersturnbull/tyrannosaurus)
[![GitHub release (latest SemVer including pre-releases)](https://img.shields.io/github/v/release/dmyersturnbull/tyrannosaurus?include_prereleases&label=GitHub)](https://github.com/dmyersturnbull/tyrannosaurus/releases)
[![Latest version on PyPi](https://badge.fury.io/py/tyrannosaurus.svg)](https://pypi.org/project/tyrannosaurus/)
[![Documentation status](https://readthedocs.org/projects/tyrannosaurus/badge/?version=latest&style=flat-square)](https://tyrannosaurus.readthedocs.io/en/stable/)
[![Build & test](https://github.com/dmyersturnbull/tyrannosaurus/workflows/Build%20&%20test/badge.svg)](https://github.com/dmyersturnbull/tyrannosaurus/actions)
[![Travis](https://img.shields.io/travis/dmyersturnbull/tyrannosaurus?label=Travis)](https://travis-ci.org/dmyersturnbull/tyrannosaurus)
[![Azure DevOps builds](https://img.shields.io/azure-devops/build/dmyersturnbull/0350c934-2512-4592-848e-9db46c63241a/1?label=Azure)](https://dev.azure.com/dmyersturnbull/tyrannosaurus/_build?definitionId=1&_a=summary)
[![Maintainability](https://api.codeclimate.com/v1/badges/5e3b38c9b9c418461dc3/maintainability)](https://codeclimate.com/github/dmyersturnbull/tyrannosaurus/maintainability)
[![Coverage](https://coveralls.io/repos/github/dmyersturnbull/tyrannosaurus/badge.svg?branch=master)](https://coveralls.io/github/dmyersturnbull/tyrannosaurus?branch=master)

An opinionated, forwards-looking Python template for 2020.
No setup.py, requirements.txt, or eggs.

I wrote this after making nearly 50 commits to configure
readthedocs, PyPi, Tox, Docker, Travis, and Github actions.
This avoids that struggle for 99% of projects.
Just clone and modify or use `tyrannosaurus new`.
Install with `pip install tyrannosaurus`.

- _When you commit_, your code is linted.
- _When you push or make a pull request_, your code is built and tested.
  Security checks are run, style is checked,
  documentation is generated, and docker images, sdists, and wheels are built.
- _When you release on Github_, your code is published to PyPi and DockerHub.
  Just add `PYPI_TOKEN` as a Github repo secret.

If you’re curious why older infrastructure (setup.py, etc) is problematic,
see [this post](https://dmyersturnbull.github.io/#-the-python-build-landscape).

⚠ Status: Alpha. Generally works well, but
   the `sync` command does less than advertised.

##### Integrations:

Also comes with nice Github labels, issue templates, a changelog template,
Travis support, Conda recipe and environment generation, and other integrations.
Tyrannosaurus itself is included as a dependency.
Running `tyrannosaurus build` will run poetry lock, synchronize project metadata, build, run tests, install,
and clean up. The project metadata is synchronized from `pyproject.toml` to other files,
such as Anaconda recipes and environment files, license headers, doc and tox requirements, and author/contributor lists.
Target files can be disabled in `[tool.tyrannosaurus.targets]`.


##### To build your own code:

To run locally, install [Poetry](https://github.com/python-poetry/poetry)
and [Tox](https://tox.readthedocs.io/en/latest/) (`pip install tox`).
Then just type `tox` to build artifacts and run tests.
To create an initial Anaconda recipe or environment file, run `tyrannosaurus recipe` or `tyrannosaurus env`.

**[See the docs](https://tyrannosaurus.readthedocs.io/en/stable/)** for more information.

##### Contributing:

[New issues](https://github.com/dmyersturnbull/tyrannosaurus/issues) and pull requests are welcome.
Please refer to the [contributing guide](https://github.com/dmyersturnbull/tyrannosaurus/blob/master/CONTRIBUTING.md).
Generated with tyrannosaurus: `tyrannosaurus new tyrannosaurus`


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
