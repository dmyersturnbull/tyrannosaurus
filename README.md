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
[![Coverage](https://coveralls.io/repos/github/dmyersturnbull/tyrannosaurus/badge.svg?branch=master&service=github)](https://coveralls.io/github/dmyersturnbull/tyrannosaurus?branch=master)

An opinionated, forwards-looking Python template for 2021.

This is a massively upgraded, trimmed-down, modern alternative to
[cookiecutter](https://github.com/cookiecutter/cookiecutter) built with [Poetry](https://python-poetry.org/),
[Tox](https://github.com/tox-dev/tox), and [Github Actions](https://github.com/features/actions).
No setup.py, requirements.txt, or eggs. If you’re curious why that infrastructure is problematic,
see [this post](https://dmyersturnbull.github.io/#-the-python-build-landscape)

I wrote this after making nearly 50 commits to configure
readthedocs, PyPi, Poetry, Tox, Docker, Travis, and Github actions.
This avoids that struggle for 99% of projects.
To generate a new project, run:

```bash
pip install tyrannosaurus
tyrannosaurus new projectname --user gituserororg --track
```

Modify the generated files (especially `pyproject.toml`) as you see fit.
Here’s how your new project will behave, by default:

- When you _commit_, your code is linted.
- When you _push or make a pull request_, your code is built and tested.
  Security checks are run, style is checked, documentation is validated, and artifacts are built.
- When you _push_ to the main branch, coverage and code quality badges are updated,
  and documentation is sent to readthedocs.
- When you _release on Github_, your code is published to PyPi and DockerHub,
  and wheels and sdists are attached to the Github release.
  (Add `PYPI_TOKEN` and `COVERALLS_REPO_TOKEN` as Github repo secrets.)
- If you run `tyrannosaurus sync`, your project metadata is synchronized to pyproject.toml

Tox, Git Pre-Commit, and Github Actions provide these behaviors.
You can modify them via `pyproject.toml`, `tox.ini`, `pre-commit-config.yml` and `.github/workflows`.

You’ll also have nice Github labels, templates for issues and pull requests, and a changelog template.
These can be modified by editing `.github/labels.json`, `.github/ISSUE_TEMPLATE`, and `CHANGELOG.md`.
Integration is also provided for Travis, Azure, Anaconda/Conda, and a few other tools.
(Azure may take a little extra to get working.)


##### Synchronization:

*Note: This feature is only partly complete.*

Tyrannosaurus has an optional `sync` command that synchronizes metadata from `pyproject.toml` to other files,
so that **all of your metadata is in pyproject.toml**.
There are 16 available target files, including `docs/conf.py`, `tox.ini`, `.pre-commit-config.yaml`, `readthedocs.yml`,
`.travis.yml`, and `__init__.py`.
Settings like dev dependencies, project version, license headers, and preferred line length can be listed exactly once,
in pyproject.toml.

Tyrannosaurus itself can be included as a dependency (but is not by default).
Running `tyrannosaurus build` will run poetry lock, synchronize project metadata (via `sync`), build, run tests,
install, and clean up.
Target files can be disabled in `[tool.tyrannosaurus.targets]`.


##### Building your project locally:

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
