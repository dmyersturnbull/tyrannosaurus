# Tyrannosaurus Reqs
[![Version status](https://img.shields.io/pypi/status/tyrannosaurus?label=status)](https://pypi.org/project/tyrannosaurus)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python version compatibility](https://img.shields.io/pypi/pyversions/tyrannosaurus?label=Python)](https://pypi.org/project/tyrannosaurus)
[![Version on Docker Hub](https://img.shields.io/docker/v/dmyersturnbull/tyrannosaurus?color=green&label=Docker%20Hub)](https://hub.docker.com/repository/docker/dmyersturnbull/tyrannosaurus)
[![Version on Github](https://img.shields.io/github/v/release/dmyersturnbull/tyrannosaurus?include_prereleases&label=GitHub)](https://github.com/dmyersturnbull/tyrannosaurus/releases)
[![Version on PyPi](https://img.shields.io/pypi/v/tyrannosaurus?label=PyPi)](https://pypi.org/project/tyrannosaurus)
[![Version on Conda-Forge](https://img.shields.io/conda/vn/conda-forge/tyrannosaurus?label=Conda-Forge)](https://anaconda.org/conda-forge/tyrannosaurus)  
[![Build (Actions)](https://img.shields.io/github/workflow/status/dmyersturnbull/tyrannosaurus/Build%20&%20test?label=Tests)](https://github.com/dmyersturnbull/tyrannosaurus/actions)
[![Build (Travis)](https://img.shields.io/travis/dmyersturnbull/tyrannosaurus?label=Travis)](https://travis-ci.org/dmyersturnbull/tyrannosaurus)
[![Documentation status](https://readthedocs.org/projects/tyrannosaurus/badge)](https://tyrannosaurus.readthedocs.io/en/stable/)
[![Coverage (coveralls)](https://coveralls.io/repos/github/dmyersturnbull/tyrannosaurus/badge.svg?branch=main&service=github)](https://coveralls.io/github/dmyersturnbull/tyrannosaurus?branch=main)
[![Coverage (codecov)](https://codecov.io/github/dmyersturnbull/tyrannosaurus/coverage.svg)](https://codecov.io/gh/dmyersturnbull/tyrannosaurus)
[![Maintainability (Code Climate)](https://api.codeclimate.com/v1/badges/5e3b38c9b9c418461dc3/maintainability)](https://codeclimate.com/github/dmyersturnbull/tyrannosaurus/maintainability)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/dmyersturnbull/tyrannosaurus/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/dmyersturnbull/tyrannosaurus/?branch=main)


An opinionated, forwards-looking Python template for 2021.

Generate elegant, ready-to-use Python
projects that have excellent continuous integration and deployment (CI/CD). Integrated with
Docker Hub, Github Packages, Azure, Conda-Forge, and an array of linting, static analysis,
security testing, documentation, dependency management, and CI/CD tools, including a custom tool
to keep all duplicate project metadata synchronized to pyproject.toml.

This is a modern alternative to cookiecutter built with [Poetry](https://python-poetry.org/),
[Github Actions](https://github.com/features/actions), and
[no legacy files](https://dmyersturnbull.github.io/#-the-python-build-landscape) or tools.
See below for a comparison to other tools.
Don’t make 55 commits trying to configure CI/CD workflows. Use `tyrannosaurus new`:


```bash
pip install tyrannosaurus
tyrannosaurus new projectname --track
```

After initializing your project, Tyrannosaurus will list some manual steps, such as adding API keys.


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
    [Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/)
  - Continuous deployment to [PyPi](http://pypi.org/), [Dockerhub](https://hub.docker.com/),
    and [Github Packages](https://github.com/features/packages).
  - Automatic attachment of [sdits](https://docs.python.org/3/distutils/sourcedist.html)
    and [wheels](https://pythonwheels.com/) to
    [Github Releases](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/about-releases)
  - Documentation sent to [readthedocs](https://readthedocs.org/)
  - Nice documentation defaults with
    [Sphinx extensions](https://www.sphinx-doc.org/en/master/usage/extensions/index.html)
  - Test automation with [Tox](https://tox.readthedocs.io)
  - [Shields](https://github.com/badges/shields) with
    [Coveralls](https://coveralls.io/),
    [codecov](https://about.codecov.io/),
    [CodeClimate](https://codeclimate.com/),
    and [Scrutinizer](https://scrutinizer-ci.com/)
    that reflect the main branch
  - Code linting with [pre-commit](https://pre-commit.com/), [Black](https://pypi.org/project/black/),
    and [Prettifier](https://prettier.io/)
  - Security analysis with [Bandit](https://github.com/PyCQA/bandit),
    [CodeQL](https://github.com/github/codeql-action),
    and [safety](https://github.com/pyupio/safety) †
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
  - `tyrannosaurus clean` to clean temp files
  - `tyrannosaurus update` that lists dependency versions to bump
  - `tyrannosaurus sync` to synchronize project metadata to pyproject.toml

† [Temporary issue in safety](https://github.com/pyupio/safety/issues/201)


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

There are various packages that can be used to generate Python projects from templates.
I think Tyrannosaurus has some very clear advantages over these:
- A highly streamlined workflow. You only need to interact directly with your project via
  `git commit`, `git push`, and creating Github releases. Everything else happens automatically.
- Integration with Docker, Docker Hub, Github Packages, and Conda-Forge.
- Built-in configuration for alternative tools (such as Travis), which can simply be deleted without issue.
- An optional tool to sync duplicate metadata to pyproject.toml.

Anyway, here are some other tools:
- [hypermodern-python](https://github.com/cjolowicz/hypermodern-python), a Python template that is as modern
  as Tyrannosaurus. It looks solid but has fewer integrations and made a few choices that I consider sub-optimal,
  such as the use of [Nox](https://github.com/theacodes/nox), which has <500 Github stars.
- [cookiecutter](https://github.com/cookiecutter/cookiecutter). This is an extremely useful package that Tyrannosaurus
  could have been written to use behind the scenes. There are a number of cookiecutter templates available, including
  some modern ones. However, I did not find any that are as feature-complete or streamlined as Tyrannosaurus.
- [cookiecutter-hypermodern-python](https://github.com/cjolowicz/cookiecutter-hypermodern-python), a cookiecutter
  template for hypermodern-python.
- [wemake-python-package](https://github.com/wemake-services/wemake-python-package), another cookiecutter template.
  This is a good package, but it has a less streamlined workflow and far fewer useful integrations
- [copier](https://github.com/copier-org/copier), which can be used to keep a project up-to-date with a remote template.
  This is a neat idea that may be useful to integrate, possibly alongside `tyrannosaurus sync`.
- [python-blueprint](https://github.com/johnthagen/python-blueprint). This is an interesting template, but it’s
  quite outdated.


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
