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
It’s technically in an alpha state, but it’s pretty solid.


#### Basic usage:

To generate a new project, run:

```bash
pip install tyrannosaurus
tyrannosaurus new projectname --user gituserororg --track
```

It’ll give you a link with some steps to follow (such as adding API keys).
Of course, you can modify the generated files however you see fit.


#### Main behavior / features:

Here’s how your new project will behave, by default:

- When you _commit_, your code is linted and files are checked.
- When you _push or make a pull request_, your code is tested,
  security checks are run, and artifacts are built.
- When you _push_ to main, badges are updated and documentation is sent
- When you _release on Github_, your code is published to PyPi and DockerHub,
  and artifacts are attached to the Github release
  (Add `PYPI_TOKEN` and `COVERALLS_REPO_TOKEN` as Github repo secrets.)
- If you run `tyrannosaurus sync`, your project metadata is synchronized to pyproject.toml

Tox, Git Pre-Commit, and Github Actions provide these behaviors.
You can modify them via `pyproject.toml`, `tox.ini`, `pre-commit-config.yml` and `.github/workflows`.

#### Extras / nice-to-haves:

You’ll also have nice Github labels, templates for issues and pull requests, and a changelog template.
These can be modified by editing `.github/labels.json`, `.github/ISSUE_TEMPLATE`, and `CHANGELOG.md`.
Integration is also provided for Travis, Azure, Anaconda/Conda, and a few other tools.


**[See the docs 📚](https://tyrannosaurus.readthedocs.io/en/stable/)** for more information.


#### Full features / integrations:

  - Packaging and dependency management with [Poetry](https://python-poetry.org/)
  - Python 3.8, 3.9, and 3.8 (3.6 and 3.7 with a small change)
  - Only modern files: *no* manifest file, setup.py, requirements.txt, setup.cfg, or eggs
  - Continuous integration with [Github Actions](https://github.com/features/actions),
    [Travis](https://www.travis-ci.com/), or [Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/) †
  - Continuous deployment to [PyPi](http://pypi.org/) and [Dockerhub](https://hub.docker.com/)
  - Automatic attachment of [sdits](https://docs.python.org/3/distutils/sourcedist.html)
    and [wheels](https://pythonwheels.com/) to [Github Releases](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/about-releases)
  - Documentation sent to [readthedocs](https://readthedocs.org/)
  - Nice documentation defaults with [Sphinx extensions](https://www.sphinx-doc.org/en/master/usage/extensions/index.html)
  - Test automation with [Tox](https://tox.readthedocs.io)
  - Code quality and coverage [badges](https://github.com/badges/shields) with [Coveralls](https://coveralls.io/),
    [codecov](https://about.codecov.io/), and [CodeClimate](https://codeclimate.com/)
    that reflect the main branch
  - Code linting with [pre-commit](https://pre-commit.com/), [Black](https://pypi.org/project/black/),
    and [Prettifier](https://prettier.io/)
  - Security analysis with [Bandit](https://github.com/PyCQA/bandit),
    [CodeQL](https://docs.github.com/en/free-pro-team@latest/github/finding-security-vulnerabilities-and-errors-in-your-code/)
    ([temporary issue](https://github.com/dmyersturnbull/tyrannosaurus/issues/7),
    and [safety](https://github.com/pyupio/safety) ([temporary issue](https://github.com/pyupio/safety/issues/201))
  - Static type analysis with [mypy](https://mypy.readthedocs.io)
  - Auto-generation and synchronization of [Conda-Forge](https://conda-forge.org/) recipes and environment YML files
  - IDE hints via [EditorConfig](https://editorconfig.org/) with good defaults for most languages
  - Nice gitignore, dockerignore; issue labels; and Github-recognized issue templates, pull request templates,
    [ChangeLog](https://keepachangelog.com), readme, license, and contributing guide
  - [CodeMeta](https://codemeta.github.io/user-guide/) and [CITATION.cff](https://citation-file-format.github.io/)
  - Dependency updating with [Dependabot](https://dependabot.com/) (disabled by default)
  - Synchronization of project metadata with [Tyrannosaurus](https://tyrannosaurus.readthedocs.io/),
    so that only pyproject.toml needs to be updated


† The Azure workflow currently only builds the Docker image.


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
  As of 2020-12, the last update was in 2020-04.
- [cookiecutter-hypermodern-python](https://github.com/cjolowicz/cookiecutter-hypermodern-python)
- [cookiecutter](https://github.com/cookiecutter/cookiecutter), which still uses setup.py
- [python-blueprint](https://github.com/johnthagen/python-blueprint), which is useful to look through
  but still uses setup.py


#### Contributing:

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
