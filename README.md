# Tyranno

[![Version status](https://img.shields.io/pypi/status/tyranno?label=Status)](https://pypi.org/project/tyrannosaurus)
[![Version on PyPi](https://badgen.net/pypi/v/tyranno?label=PyPi)](https://pypi.org/project/tyrannosaurus)
[![Version on GitHub](https://badgen.net/github/release/dmyersturnbull/tyrannosaurus/stable?label=GitHub)](https://github.com/dmyersturnbull/tyrannosaurus/releases)
[![Version on Docker Hub](https://img.shields.io/docker/v/dmyersturnbull/tyrannosaurus?color=green&label=Docker%20Hub)](https://hub.docker.com/repository/docker/dmyersturnbull/tyrannosaurus)
[![Build (Actions)](https://img.shields.io/github/workflow/status/dmyersturnbull/tyrannosaurus/maintest?label=Tests)](https://github.com/dmyersturnbull/tyrannosaurus/actions)
[![Documentation status](https://readthedocs.org/projects/tyrannosaurus/badge)](https://tyranno.readthedocs.io/en/stable/)
[![Coverage (coveralls)](https://badgen.net/coveralls/c/github/dmyersturnbull/tyrannosaurus?label=Coveralls)](https://coveralls.io/github/dmyersturnbull/tyrannosaurus?branch=main)
[![Coverage (codecov)](https://badgen.net/codecov/c/github/dmyersturnbull/tyrannosaurus?label=CodeCov)](https://codecov.io/gh/dmyersturnbull/tyrannosaurus)
[![Maintainability (Code Climate)](https://badgen.net/codeclimate/maintainability/dmyersturnbull/tyrannosaurus)](https://codeclimate.com/github/dmyersturnbull/tyrannosaurus/maintainability)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/dmyersturnbull/tyrannosaurus/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/dmyersturnbull/tyrannosaurus/?branch=main)
[![CodeFactor](https://www.codefactor.io/repository/github/dmyersturnbull/tyrannosaurus/badge)](https://www.codefactor.io/repository/github/dmyersturnbull/tyrannosaurus)
[![License](https://badgen.net/pypi/license/tyrannosaurus?label=License)](https://opensource.org/licenses/Apache-2.0)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4485186.svg)](https://doi.org/10.5281/zenodo.4485186)
[![Created with Tyranno](https://img.shields.io/badge/Created_with-Tyranno-0000ff.svg)](https://github.com/dmyersturnbull/tyrannosaurus)

Tyranno is a highly streamlined modern Python template
backed by [Hatch](https://hatch.pypa.io/), pre-commit, commitizen, static analysis tools, and GitHub Actions.
Automagically works with Docker, container registries, Conda, readthedocs, GitHub Pages.
Optionally add `:tyranno:` comments to sync project metadata like versions every time you commit.

The focus is on automation and modern tooling. Poke around this repo to get the feel.
Clone to get started. Installing [Probot settings](https://github.com/probot/settings) is also recommended.

- `git commit` will format and run basic linting via pre-commit.
- Run `hatch test` to test locally. Use `hatch lint` to lint.
- Open a pull request, and it'll get labeled automatically (assuming conventional commits),
  and tested in the cloud.
- Squash that request into _main_ to deploy docs and update coverage reports.
- `hatch bump` to bump the version automatically, tag the commit, and update `CHANGELOG.md`.
- Push a new `v*` tag to deploy to GitHub, PyPi, Docker Hub, the GCR, GitHub Pages, and readthedocs.
  GitHub release notes are automatically generated, and Docker images are fully tagged.

Your responsibilities are only to write decent commit messages, especially when squashing into _main_.
That and to run a few commands and otherwise focus on coding.
Everything else happens automagically through a bunch of great third-party tools.
Don’t make 150 commits for CI/CD. This one works probably works better.
[📚 See the docs](https://readthedocs.org/projects/tyranno) for details.

### 🎯 Similar templates and tools

There are various other templates based on [cookiecutter](https://github.com/cookiecutter/cookiecutter)
and [copier](https://github.com/copier-org/copier). See which best suits your needs and style.

I designed Tyranno to solve issues with existing tools.
I wanted:

[x] An **elegant CI/CD workflow**: Workflows are kicked off only by `git push`.
[x] **Automated publishing** to PyPi and container registries.
[x] _No duplication_ between project files.
[x] Complete **absence of legacy tools**, files, and Python 2 support.

### 🏁 Feature table

| Tool                                                                                | Main CD | Docker CD  | Build  | Test   | Conv. Comm. | Lint   | any-OS | Bootstrap | Sync |
| ----------------------------------------------------------------------------------- | ------- | ---------- | ------ | ------ | ----------- | ------ | ------ | --------- | ---- |
| Tyranno                                                                             | Actions | GHCR, DH   | Hatch  | Hatch  | cz, Actions | Ruff   | y      | y         | y    |
| [hypermodern-python](https://github.com/cjolowicz/cookiecutter-hypermodern-python)  | Poetry  |            | Poetry | Nox    |             | misc.  | y      |           |      |
| ~~[python-package-template](https://github.com/TezRomacH/python-package-template)~~ | Poetry  |            | Poetry | Make   |             | Flake8 |        |           |      |
| [pyscaffold](https://github.com/pyscaffold/pyscaffold)                              | Tox     |            | legacy | Tox    |             | Flake8 | y      |           |      |
| [wemake-python-package](https://github.com/wemake-services/wemake-python-package)   | Poetry  |            | Poetry | Make   |             | Flake  |        |           |      |
| [best-practices](https://github.com/sourcery-ai/python-best-practices-cookiecutter) |         | deprecated | pipenv | pipenv |             | Flake8 | y      |           |      |
| [python-blueprint](https://github.com/johnthagen/python-blueprint)                  | Actions |            | Poetry | Tox    |             | Ruff   | y      |           |      |
| [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)   |         |            | legacy | Nox    |             | Flake8 |        |           |      |
| [cookiecutter-pylibrary](https://github.com/ionelmc/cookiecutter-pylibrary)         |         |            | legacy | Tox    |             | Ruff   | y      |           |      |
| [cookiecutter-django](https://github.com/pydanny/cookiecutter-django)               | Actions |            | legacy | Tox    |             | Flake8 | y      |           |      |
| [django-init](https://github.com/Fueled/django-init)                                | Poetry  |            | legacy | Make   |             | Flake8 | y      |           |      |
| ~~[docker-science](https://github.com/docker-science/cookiecutter-docker-science)~~ |         |            | legacy | Make   |             |        |        |           |      |

### 🍁 Contributing

[New issues](https://github.com/dmyersturnbull/tyranno/issues) and pull requests are welcome.
Please refer to the [contributing guide](https://github.com/dmyersturnbull/tyranno/blob/master/CONTRIBUTING.md)
and [security policy](https://github.com/dmyersturnbull/tyranno/blob/main/SECURITY.md).
Generated with tyranno: `tyranno new tyranno`

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
