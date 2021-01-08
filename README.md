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
[![Maintainability](https://api.codeclimate.com/v1/badges/5e3b38c9b9c418461dc3/maintainability)](https://codeclimate.com/github/dmyersturnbull/tyrannosaurus/maintainability)
[![Coverage (coveralls)](https://coveralls.io/repos/github/dmyersturnbull/tyrannosaurus/badge.svg?branch=master&service=github)](https://coveralls.io/github/dmyersturnbull/tyrannosaurus?branch=master)
[![Coverage (codecov)](https://codecov.io/github/dmyersturnbull/tyrannosaurus/coverage.svg)](https://codecov.io/gh/dmyersturnbull/tyrannosaurus/)

An opinionated, forwards-looking Python template for 2021.  
Generate elegant, ready-to-use Python projects that have excellent continuous integration and deployment.

This is an upgraded, trimmed-down, modern alternative to
[cookiecutter](https://github.com/cookiecutter/cookiecutter) built with [Poetry](https://python-poetry.org/),
[Tox](https://github.com/tox-dev/tox), and [Github Actions](https://github.com/features/actions).
[No legacy files](https://dmyersturnbull.github.io/#-the-python-build-landscape) or tools.

Don’t make 55 commits trying to configure Travis, Docker, or readthedocs. Just use `tyrannosaurus new`


```bash
pip install tyrannosaurus
tyrannosaurus new projectname --user gituserororg --track
```

Tyrannosaurus will then list final manual steps like adding API keys.  
(`--track` will git track _gituserororg/projectname_.)


#### Main behavior / features:

Generated projects are integrated with various tools (from PyPi) and external CI/CD/code-quality systems.
Github Actions are used by default, but config files for Travis and Azure Pipelines are also provided.
You can swap out, modify, or disable anything as you see fit.
**[See the docs 📚](https://tyrannosaurus.readthedocs.io/en/stable/)** for more information.

*By default*, here’s how your new project will behave:

- **Commit** ⇒ Files are linted and verified for integrity
- **Make a pull request** ⇒ Code is built and tested
- **Push to the main branch** ⇒ Code is built and tested; code quality, coverage, and security badges are updated
- **Make a Github release** ⇒ Artifacts are sent to Github, PyPi, DockerHub, Github Packages, and readthedocs
- `tox` ⇒ Tests are run locally
- `tyrannosaurus sync` ⇒ Project metadata is synced to pyproject.toml
- `tyrannosaurus update` ⇒ New dependency versions from PyPi and/or Conda are listed


#### Full features / integrations:

  - Packaging and dependency management with [Poetry](https://python-poetry.org/)
  - Python 3.8, 3.9, and 3.10 (3.6 and 3.7 with a small change)
  - Only modern files: *no* manifest file, setup.py, requirements.txt, setup.cfg, or eggs
  - Continuous integration with [Github Actions](https://github.com/features/actions),
    [Travis](https://www.travis-ci.com/), or
    [Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/) †
  - Continuous deployment to [PyPi](http://pypi.org/), [Dockerhub](https://hub.docker.com/),
    and [Github Packages](https://github.com/features/packages).
  - Automatic attachment of [sdits](https://docs.python.org/3/distutils/sourcedist.html)
    and [wheels](https://pythonwheels.com/) to
    [Github Releases](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/about-releases)
  - Documentation sent to [readthedocs](https://readthedocs.org/)
  - Nice documentation defaults with
    [Sphinx extensions](https://www.sphinx-doc.org/en/master/usage/extensions/index.html)
  - Test automation with [Tox](https://tox.readthedocs.io)
  - Code quality and coverage [badges](https://github.com/badges/shields) with [Coveralls](https://coveralls.io/),
    [codecov](https://about.codecov.io/), and [CodeClimate](https://codeclimate.com/)
    that reflect the main branch
  - Code linting with [pre-commit](https://pre-commit.com/), [Black](https://pypi.org/project/black/),
    and [Prettifier](https://prettier.io/)
  - Security analysis with [Bandit](https://github.com/PyCQA/bandit),
    [CodeQL](https://github.com/github/codeql-action),
    and [safety](https://github.com/pyupio/safety) ‡
  - Static type analysis with [mypy](https://mypy.readthedocs.io)
  - [Conda-Forge](https://conda-forge.org/) [recipes](https://conda-forge.org/docs/maintainer/adding_pkgs.html#the-recipe-meta-yaml)
    and [environment YML](https://medium.com/@balance1150/how-to-build-a-conda-environment-through-a-yaml-file-db185acf5d22)
    with [Grayskull](https://github.com/conda-incubator/grayskull)
    and [Tyrannosaurus](https://tyrannosaurus.readthedocs.io/)
  - IDE hints via [EditorConfig](https://editorconfig.org/) with good defaults for most languages
  - Fancy [issue labels](https://github.com/crazy-max/ghaction-github-labeler)
  - Fancy Github-recognized readme, license,
    [contributing guide](https://docs.github.com/en/free-pro-team@latest/github/building-a-strong-community/setting-guidelines-for-repository-contributors#adding-a-contributing-file),
    [issue templates](https://docs.github.com/en/free-pro-team@latest/github/building-a-strong-community/configuring-issue-templates-for-your-repository), and
    [pull request templates](https://docs.github.com/en/free-pro-team@latest/github/building-a-strong-community/creating-a-pull-request-template-for-your-repository)
  - Nice gitignore, dockerignore, [ChangeLog](https://keepachangelog.com), and other misc files
  - [CodeMeta](https://codemeta.github.io/user-guide/) and [CITATION.cff](https://citation-file-format.github.io/)
  - Dependency updating with [Dependabot](https://dependabot.com/)
  - Auto cleanup of useless files (on running tox); `tyrannosaurus clean` to clean all temp files
  - `tyrannosaurus update` that lists dependency versions to bump
  - `tyrannosaurus sync` to synchronize project metadata to pyproject.toml

† Currently, the Azure pipeline config only builds a Docker image.  
‡ [Temporary issue in safety](https://github.com/pyupio/safety/issues/201)


#### Syncing to pyproject.toml:

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


#### Building your project locally:

To run locally, install [Poetry](https://github.com/python-poetry/poetry)
and [Tox](https://tox.readthedocs.io/en/latest/) (`pip install tox`).
Then just type `tox` to build artifacts and run tests.
To create an initial Anaconda recipe or environment file, run `tyrannosaurus recipe` or `tyrannosaurus env`.


#### Similar tools:

- [hypermodern-python](https://github.com/cjolowicz/hypermodern-python), a Python template that is similarly modern.
  It looks solid but has fewer integrations.
  A few choices were different, such as the use of [Nox](https://github.com/theacodes/nox).
  Nox has less traction and <500 Github stars, and was not updated since 2020-04 as of 2020-12.
- [cookiecutter-hypermodern-python](https://github.com/cjolowicz/cookiecutter-hypermodern-python)
- [cookiecutter](https://github.com/cookiecutter/cookiecutter), which still uses setup.py
- [python-blueprint](https://github.com/johnthagen/python-blueprint), which is useful to look through
  but still uses setup.py


#### Contributing:

[New issues](https://github.com/dmyersturnbull/tyrannosaurus/issues) and pull requests are welcome.
Please refer to the [contributing guide](https://github.com/dmyersturnbull/tyrannosaurus/blob/master/CONTRIBUTING.md)
and [security policy](https://github.com/dmyersturnbull/tyrannosaurus/blob/main/SECURITY.md).  
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
