# Tyrannosaurus

[![Version status](https://img.shields.io/pypi/status/tyrannosaurus?label=status)](https://pypi.org/project/tyrannosaurus)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python version compatibility](https://img.shields.io/pypi/pyversions/tyrannosaurus?label=Python)](https://pypi.org/project/tyrannosaurus)
[![Version on Docker Hub](https://img.shields.io/docker/v/dmyersturnbull/tyrannosaurus?color=green&label=Docker%20Hub)](https://hub.docker.com/repository/docker/dmyersturnbull/tyrannosaurus)
[![Version on GitHub](https://img.shields.io/github/v/release/dmyersturnbull/tyrannosaurus?include_prereleases&label=GitHub)](https://github.com/dmyersturnbull/tyrannosaurus/releases)
[![Version on PyPi](https://img.shields.io/pypi/v/tyrannosaurus?label=PyPi)](https://pypi.org/project/tyrannosaurus)
[![Version on Conda-Forge](https://img.shields.io/conda/vn/conda-forge/tyrannosaurus?label=Conda-Forge)](https://anaconda.org/conda-forge/tyrannosaurus)  
[![Build (Actions)](https://img.shields.io/github/workflow/status/dmyersturnbull/tyrannosaurus/Build%20&%20test?label=Tests)](https://github.com/dmyersturnbull/tyrannosaurus/actions)
[![Build (Travis)](https://img.shields.io/travis/dmyersturnbull/tyrannosaurus?label=Travis)](https://travis-ci.org/dmyersturnbull/tyrannosaurus)
[![Documentation status](https://readthedocs.org/projects/tyrannosaurus/badge)](https://tyrannosaurus.readthedocs.io/en/stable/)
[![Coverage (coveralls)](https://coveralls.io/repos/github/dmyersturnbull/tyrannosaurus/badge.svg?branch=main&service=github)](https://coveralls.io/github/dmyersturnbull/tyrannosaurus?branch=main)
[![Coverage (codecov)](https://codecov.io/github/dmyersturnbull/tyrannosaurus/coverage.svg)](https://codecov.io/gh/dmyersturnbull/tyrannosaurus)
[![Maintainability (Code Climate)](https://api.codeclimate.com/v1/badges/5e3b38c9b9c418461dc3/maintainability)](https://codeclimate.com/github/dmyersturnbull/tyrannosaurus/maintainability)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/dmyersturnbull/tyrannosaurus/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/dmyersturnbull/tyrannosaurus/?branch=main)  
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4485186.svg)](https://doi.org/10.5281/zenodo.4485186)
[![Created with Tyrannosaurus](https://img.shields.io/badge/Created_with-Tyrannosaurus-0000ff.svg)](https://github.com/dmyersturnbull/tyrannosaurus)

An opinionated, forwards-looking Python template for 2021.

Generate elegant, ready-to-use Python
projects that have excellent continuous integration and deployment (CI/CD). Integrated with
Docker Hub, GitHub Packages, Azure, Conda-Forge, and an array of linting, static analysis,
security testing, documentation, dependency management, and CI/CD tools, including an optional
custom tool to keep all duplicate project metadata synchronized to pyproject.toml.

### 🎨 Design / generating a new project

This is a modern template built with [Poetry](https://python-poetry.org/),
[GitHub Actions](https://github.com/features/actions), and
[no legacy files](https://dmyersturnbull.github.io/#-the-python-build-landscape) or tools.
See below for a [comparison to other tools](https://github.com/dmyersturnbull/tyrannosaurus#-similar-templates-and-tools).
Also see Tyrannosaurus’s little sister
[science-notebook-template 🧪](https://github.com/dmyersturnbull/science-notebook-template)
for repos supporting scientific publications.

Don’t make 55 commits trying to configure CI/CD workflows.

```bash
pip install tyrannosaurus
tyrannosaurus new projectname --track
```

After initializing your project, Tyrannosaurus will list manual steps like adding API keys.

### 💡 Main behavior / features

Generated projects are integrated with various tools (from PyPi) and external CI/CD/code-quality systems.
GitHub Actions are used by default, but config files for Travis and Azure Pipelines are also provided.
You can swap out, modify, or disable anything as you see fit.
**[See the docs 📚](https://tyrannosaurus.readthedocs.io/en/stable/)** for more information.

_By default_, here’s how your new project will behave:

- **Commit** ⇒ Files are linted and verified for integrity
- **Make a pull request** ⇒ Code is built and tested
- **Push to the main branch** ⇒ Code is built and tested; code quality, coverage, and security badges are updated
- **Make a GitHub release** ⇒ Artifacts are sent to GitHub, PyPi, DockerHub, GitHub Packages, and readthedocs
- `tox` ⇒ Tests are run locally
- `tyrannosaurus sync` ⇒ Project metadata is synced to pyproject.toml
- `tyrannosaurus update` ⇒ New dependency versions from PyPi and/or Conda are listed

### 🎁 Full features / integrations

- Packaging and dependency management with [Poetry](https://python-poetry.org/)
- Python 3.8, 3.9, and 3.10 (3.6 and 3.7 with a small change)
- Only modern files: _no_ manifest file, setup.py, requirements.txt, setup.cfg, or eggs
- Continuous integration with [GitHub Actions](https://github.com/features/actions),
  [Travis](https://www.travis-ci.com/), or
  [Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/)
- Docker and Vagrant configuration
- Continuous deployment to [PyPi](http://pypi.org/), [Dockerhub](https://hub.docker.com/),
  and [GitHub Packages](https://github.com/features/packages).
- Automatic attachment of [sdits](https://docs.python.org/3/distutils/sourcedist.html)
  and [wheels](https://pythonwheels.com/) to
  [GitHub Releases](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/about-releases)
- Good default GitHub settings, synchronized via [Probot settings](https://github.com/probot/settings)
- Documentation sent to [readthedocs](https://readthedocs.org/)
- Nice documentation defaults with
  [Sphinx extensions](https://www.sphinx-doc.org/en/master/usage/extensions/index.html)
- Test automation with [Tox](https://tox.readthedocs.io)
- Commit linting and changelog generation with [Commitizen](https://github.com/commitizen-tools/commitizen)
- [Shields](https://github.com/badges/shields) with
  [Coveralls](https://coveralls.io/),
  [codecov](https://about.codecov.io/),
  [CodeClimate](https://codeclimate.com/),
  and [Scrutinizer](https://scrutinizer-ci.com/)
  that reflect the main branch
- Code linting with [pre-commit](https://pre-commit.com/), [Black](https://pypi.org/project/black/),
  [Prettifier](https://prettier.io/), [Dockerfile-lint](https://github.com/Lucas-C/pre-commit-hooks-nodejs),
  and [markdown-lint-check](https://github.com/gaurav-nelson/github-action-markdown-link-check)
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
- Slack notifications for CI/CD success and failure with [action-slack](https://github.com/8398a7/action-slack)
- Fancy GitHub-recognized readme, license,
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

### ✏️ Syncing to pyproject.toml

_Note: This feature is only partly complete._

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

### 🔨 Building your project locally

You can test your project locally. Install [Poetry](https://github.com/python-poetry/poetry)
and [Tox](https://tox.readthedocs.io/en/latest/) (`pip install tox`).
Then just type `tox` to build artifacts and run tests.
You can install locally with `poetry install .` or just `pip install .`.
To create an initial Anaconda recipe or environment file, run `tyrannosaurus recipe` or `tyrannosaurus env`.
After that, you can use `sync` to keep them up-to-date with pyproject.toml.

### 🎯 Similar templates and tools

There are various other templates based on [cookiecutter](https://github.com/cookiecutter/cookiecutter)
and [copier](https://github.com/copier-org/copier). See which best suits your needs and style.

I designed Tyrannosaurus to solve issues with existing tools.
Here are features that other tools lack:

- An **elegant CI/CD workflow**: The workflow gets kicked off only via `git push` and GitHub releases.
- **Interopability with Conda**, including recipes and environment files, by mapping dependencies and metadata.
- **Automated publishing** to PyPi, Conda-Forge, Docker Hub, GitHub Packages, and readthedocs.
- **No duplication** between project files. (Not 100%: some duplication remains.)
- Built-in optional support for **extra/alternative tools**, such as Travis and codemeta.
- Complete **absence of legacy tools**, files, and Python 2 support.

##### 🏁 Feature table

[science-notebook-template 🧪](https://github.com/dmyersturnbull/science-notebook-template)

| Tool                                                                                     | Main techs                | CD kickoff  | N int.† | modern‡ | Docker | Conda | sync | Django |
| ---------------------------------------------------------------------------------------- | ------------------------- | ----------- | ------- | ------- | ------ | ----- | ---- | ------ |
| Tyranosaurus                                                                             | Actions, Poetry, Tox      | git, GitHub | 30      | ✔️      | ✔️     | ✔️    | ✔️   |        |
| [hypermodern-python](https://github.com/cjolowicz/cookiecutter-hypermodern-python)       | Actions, Poetry, Nox      | git, Poetry | 20      | ✔️      |        |       |      |        |
| [copier-poetry](https://github.com/pawamoy/copier-poetry)                                | Actions, Poetry, Make     | git, manual | 15      |         | ✔️     |       | ✔️   |        |
| [wemake-python-package](https://github.com/wemake-services/wemake-python-package)        | Actions, Poetry, Make     | git, Poetry | 10      | ✔️      |        |       |      |        |
| [best-practices](https://github.com/sourcery-ai/python-best-practices-cookiecutter)      | Actions, pipenv           | git, pipenv | 10      |         | ✔️     |       |      |        |
| [python-blueprint](https://github.com/johnthagen/python-blueprint)                       | Actions, setuptools, Tox  | git, manual | 5       |         | ✔️     |       |      |        |
| [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)        | Travis, setuptools, Tox   | git, manual | 10      |         |        |       |      |        |
| [cookiecutter-pylibrary](https://github.com/ionelmc/cookiecutter-pylibrary)              | Travis, setuptools, Tox   | git, manual | 20      |         |        |       |      |        |
| [cookiecutter-django](https://github.com/pydanny/cookiecutter-django)                    | Actions, setuptools, Tox  | git, manual | 15      |         | ✔️     |       |      | ✔️     |
| [django-init](https://github.com/Fueled/django-init)                                     | Actions, setuptools, Make | git, manual | 15      |         | ✔️     |       |      | ✔️     |
| [docker-science](https://github.com/docker-science/cookiecutter-docker-science)          | Make, Docker, setuptools  | no CI/CD    | 15      |         | ✔️     |       |      |        |
| [science-notebook-template](https://github.com/dmyersturnbull/science-notebook-template) | Conda                     | no CI/CD    | 5       |         | ✔️     |       |      |        |

**† _N int._**: Approximate number of built-in integrations with tools and standards. What counts is very roughly defined.  
**‡ _Modern_**: Lacks legacy files and tools. I’m including Make, setuptools, pipenv, and some others.  
**Note:** [copier](https://github.com/copier-org/copier) syncs with a remote template. It’s a neat idea that Tyrannosaurus lacks.

Some of the packages in the table above need more explanation:

- [hypermodern-python](https://github.com/cjolowicz/hypermodern-python)
  ([template](https://github.com/cjolowicz/cookiecutter-hypermodern-python)), a Poetry-powered Python
  template. It’s good, but it made a few unusual choices, such as [Nox](https://github.com/theacodes/nox), which has <500 GitHub stars.
- Both [cookiecutter-django](https://github.com/pydanny/cookiecutter-django) and
  [django-init](https://github.com/Fueled/django-init) have fantastic setups for Django projects.
- [Cookiecutter-docker-science](https://github.com/docker-science/cookiecutter-docker-science) is an interesting project
  that doesn’t quite fit in this list.

### 🍁 Contributing

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
