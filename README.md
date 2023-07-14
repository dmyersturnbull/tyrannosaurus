# Tyranno

[![Version status](https://img.shields.io/pypi/status/tyranno?label=Status)](https://pypi.org/project/tyranno)<!--<< :tyranno: [![Version status](https://img.shields.io/pypi/status/${.name}?label=Status)](https://pypi.org/project/${.name}) -->
[![Version on PyPi](https://badgen.net/pypi/v/tyranno?label=PyPi)](https://pypi.org/project/tyranno)<!--<< :tyranno: [![Version on PyPi](https://badgen.net/pypi/v/${.name}?label=PyPi -->
[![Version on GitHub](https://badgen.net/github/release/dmyersturnbull/tyranno/stable?label=GitHub)](https://github.com/dmyersturnbull/tyranno/releases)<!--<< :tyranno: [![Version on GitHub](https://badgen.net/github/release/${.frag}/stable?label=GitHub)](${.link.repo}/releases) -->
[![Version on Docker Hub](https://img.shields.io/docker/v/dmyersturnbull/tyranno?color=green&label=Docker%20Hub)](https://hub.docker.com/repository/docker/dmyersturnbull/tyranno)<!--<< :tyranno: [![Version on Docker Hub](https://img.shields.io/docker/v/dmyersturnbull/tyranno?color=green&label=Docker%20Hub)](https://hub.docker.com/repository/docker/${.frag}) -->
[![Version on Conda-Forge](https://img.shields.io/conda/vn/conda-forge/tyranno?label=Conda-Forge)](https://anaconda.org/conda-forge/tyranno)<!--<< :tyranno: [![Version on Conda-Forge](https://img.shields.io/conda/vn/conda-forge/${.name}?label=Conda-Forge)](https://anaconda.org/conda-forge/${T.name})\ -->

[![Build (Actions)](https://img.shields.io/github/workflow/status/dmyersturnbull/tyranno/maintest?label=Tests)](https://github.com/dmyersturnbull/tyranno/actions)<!--<< :tyranno: [![Build (Actions)](https://img.shields.io/github/workflow/status/${T.name}/${.org}/maintest?label=Tests)](${.link.url}/actions) -->
[![Documentation status](https://readthedocs.org/projects/tyranno/badge)](https://tyranno.readthedocs.io/en/stable/)<!--<< :tyranno: [![Documentation status](${.link.url}/badge)](${.link.docs}) -->
[![Coverage (coveralls)](https://badgen.net/coveralls/c/github/dmyersturnbull/tyranno?label=Coveralls)](https://coveralls.io/github/dmyersturnbull/tyranno?branch=main)<!--<< :tyranno: [![Coverage (coveralls)](https://badgen.net/coveralls/c/github/${T.name}/${.name}?label=Coveralls)](https://coveralls.io/github/${.frag}?branch=main) -->
[![Coverage (codecov)](https://badgen.net/codecov/c/github/dmyersturnbull/tyranno?label=CodeCov)](https://codecov.io/gh/dmyersturnbull/tyranno)<!--<< :tyranno: [![Coverage (codecov)](https://badgen.net/codecov/c/github/${.frag}?label=CodeCov)](https://codecov.io/gh/${.frag})\ -->

[![Maintainability (Code Climate)](https://badgen.net/codeclimate/maintainability/dmyersturnbull/tyranno)](https://codeclimate.com/github/dmyersturnbull/tyranno/maintainability)<!--<< :tyranno: [![Maintainability (Code Climate)](https://badgen.net/codeclimate/maintainability/${.frag})](https://codeclimate.com/github/${.frag}/maintainability) -->
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/dmyersturnbull/tyranno/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/dmyersturnbull/tyranno/?branch=main)<!--<< :tyranno: [![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/${.frag}/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/${.frag}/?branch=main) -->
[![CodeFactor](https://www.codefactor.io/repository/github/dmyersturnbull/tyranno/badge)](https://www.codefactor.io/repository/github/dmyersturnbull/tyranno)<!--<< :tyranno: [![CodeFactor](https://www.codefactor.io/repository/github/${.frag}/badge)](https://www.codefactor.io/repository/github/${.frag}) -->

[![License](https://badgen.net/pypi/license/tyranno?label=License)](https://opensource.org/licenses/Apache-2.0)<!--<< :tyranno: [![License](https://badgen.net/pypi/license/${.name}?label=License)](${.license.url}) -->
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4485186.svg)](https://doi.org/10.5281/zenodo.4485186)<!--<< :tyranno: [![DOI](https://zenodo.org/badge/DOI/${.doi}.svg)](https://doi.org/${.doi}) -->
[![Created with Tyranno](https://img.shields.io/badge/Created_with-Tyranno-0000ff.svg)](https://github.com/dmyersturnbull/tyranno)<!--<< :tyranno: [![Created with ${.Name}](https://img.shields.io/badge/Created_with-${.Name}-0000ff.svg)](https://github.com/${.frag}) -->

Tyranno is an ultra-modern Python project generator and tool to sync project metadata to `pyproject.toml`.

Run `tyranno new my-org/my-project`.
Add `:tyranno:` comments where wanted and run `git commit` to sync and lint.
To test, run `tox` or open a pull request against the _main_ branch.
Merge or rebase to run final tests and update coveralls or codecov.
Push a semver tag to publish to PyPi, GitHub, GHCR, and Docker Hub.

Follow conventional commits to have pull requests auto-labeled and consistent release notes
generated to `CHANGELOG.md` and your GitHub Releases.
Generate Conda-Forge recipes with `tyranno recipe` and `environment.yaml` with `tyranno env`.
Run `tyranno reqs` to list or accept Poetry updates.

[📚 See the docs](https://readthedocs.org/projects/tyranno) for details.

## 🎨 Design / generating a new project

Don’t make 150 commits trying to configure CI/CD workflows. Tyranno's just works.

`tyranno new` generates ready-to-use Python projects with outstanding CI/CD.
Integrated with Docker Hub, the GitHub Container Registry, Azure, Conda-Forge,
and an array of linting, static analysis, security testing, documentation, dependency management, CI/CD tools,
and `:tyranno:` substitutions that reduce headaches.

It uses [Poetry](https://python-poetry.org/), [GitHub Actions](https://github.com/features/actions), and
[no legacy files and tools](https://dmyersturnbull.github.io/#-the-python-build-landscape).
See below for a [comparison to other tools](https://github.com/dmyersturnbull/tyranno#-similar-templates-and-tools).
Also see Tyranno’s little sister
[science-notebook-template 🧪](https://github.com/dmyersturnbull/science-notebook-template)
for scientific publication repos.

```bash
pip install tyranno
tyranno new https://github.com/myorg/myproject.git

# Cloned https://github.com/myorg/myproject.git
# See https://tyranno.readthedocs.io/en/latest/guide.html
```

### 💡 New project behavior

This section describes how freshly `tyranno new`-ed projects work.
However, you can swap out, modify, or disable anything as you see fit.
**[See the docs 📚](https://tyranno.readthedocs.io/en/stable/)** for more information.

Here’s how your new project will behave when first set up, if appropriate secrets are set.

- **Commit** ⇒ Files are linted and verified for integrity.
- **Make a pull request** ⇒ Code is built and tested.
- **Push to the main branch** ⇒ Code is built and tested; code quality, coverage, and security badges are updated
- **Push a `v.*` tag** ⇒ Artifacts are sent to GitHub, PyPi, Docker Hub, the GCR, and readthedocs.
- `tox` ⇒ Tests are run locally
- `tyranno sync` ⇒ Project metadata is synced to pyproject.toml
- `tyranno reqs` ⇒ New dependency versions from PyPi and/or Conda are listed
- `tyranno clean` ⇒ Remove temp files

## 🎁 Features & integrations

- Packaging and dependency management with [Poetry](https://python-poetry.org/)
- Python 3.7 thru 3.12
- Only modern files: _no_ manifest file, setup.py, requirements.txt, setup.cfg, or eggs
- Continuous integration with [GitHub Actions](https://github.com/features/actions),
  [Travis](https://www.travis-ci.com/), or
  [Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/)
- Docker and Vagrant configuration
- Continuous deployment to [PyPi](http://pypi.org/) and [Docker Hub](https://hub.docker.com/).
- Deployment to the [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry);
  plus to any other desired container registries with a simple modification.
- Automatic attachment of [sdits](https://docs.python.org/3/distutils/sourcedist.html)
  and [wheels](https://pythonwheels.com/) to
  [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
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
  and [safety](https://github.com/pyupio/safety)
- Static type analysis with [mypy](https://mypy.readthedocs.io)
- [Conda-Forge](https://conda-forge.org/) [recipes](https://conda-forge.org/docs/maintainer/adding_pkgs.html#the-recipe-meta-yaml)
  and [environment YML](https://medium.com/@balance1150/how-to-build-a-conda-environment-through-a-yaml-file-db185acf5d22)
  with [Grayskull](https://github.com/conda-incubator/grayskull)
  and [Tyranno](https://tyranno.readthedocs.io/)
- IDE hints via [EditorConfig](https://editorconfig.org/) with good defaults for most languages
- Fancy [issue labels](https://github.com/crazy-max/ghaction-github-labeler)
- Fancy GitHub-recognized readme, license,
  [contributing guide](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors),
  [issue templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates), and
  [pull request templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates)
- Nice gitignore, dockerignore, [ChangeLog](https://keepachangelog.com), and other misc files
- [CodeMeta](https://codemeta.github.io/user-guide/) and [CITATION.cff](https://citation-file-format.github.io/)
- Dependency updating with [Dependabot](https://dependabot.com/)
- `tyranno clean` to clean temp files
- `tyranno reqs` that lists dependency versions to bump
- `tyranno sync` to synchronize project metadata to pyproject.toml

### 🎯 Similar templates and tools

There are various other templates based on [cookiecutter](https://github.com/cookiecutter/cookiecutter)
and [copier](https://github.com/copier-org/copier). See which best suits your needs and style.

I designed Tyranno to solve issues with existing tools.
Here are features that other tools lack:

- An **elegant CI/CD workflow**: The workflow gets kicked off only via `git push` and GitHub releases.
- **Interoperability with Conda**, including recipes and environment files, by mapping dependencies and metadata.
- **Automated publishing** to PyPi, Conda-Forge, Docker Hub, the GitHub Container Registry, and readthedocs.
- **No duplication** between project files. (Not 100%: some duplication remains.)
- Built-in optional support for **extra/alternative tools**, such as Travis and codemeta.
- Complete **absence of legacy tools**, files, and Python 2 support.

### 🏁 Feature table

| Tool                                                                                     | Main techs                 | CD kickoff     | N int.† | modern‡ | Docker | Conda | sync | any-OS |
| ---------------------------------------------------------------------------------------- | -------------------------- | -------------- | ------- | ------- | ------ | ----- | ---- | ------ |
| Tyranosaurus                                                                             | Actions, Poetry, Tox       | git, GitHub    | 30      | ✔️      | ✔️     | ✔️    | ✔️   | ✔️     |
| [hypermodern-python](https://github.com/cjolowicz/cookiecutter-hypermodern-python)       | Actions, Poetry, Nox       | git, Poetry    | 20      | ✔️      |        |       |      | ✔️     |
| [copier-poetry](https://github.com/pawamoy/copier-poetry)                                | Actions, Poetry, Make      | git, manual    | 15      |         | ✔️     |       | ✔️   |        |
| [python-package-template](https://github.com/TezRomacH/python-package-template)          | Actions, Poetry, Tox, Make | git, Make      | 20      | ✔️      | ✔️     |       |      |        |
| [pyscaffold](https://github.com/pyscaffold/pyscaffold)                                   | setuptools, Tox            | Gitlab, manual | 10      |         |        |       |      | ✔️     |
| [wemake-python-package](https://github.com/wemake-services/wemake-python-package)        | Actions, Poetry, Make      | git, Poetry    | 10      | ✔️      |        |       |      |        |
| [best-practices](https://github.com/sourcery-ai/python-best-practices-cookiecutter)      | Actions, pipenv            | git, pipenv    | 10      |         | ✔️     |       |      | ✔️     |
| [python-blueprint](https://github.com/johnthagen/python-blueprint)                       | Actions, setuptools, Tox   | git, manual    | 5       |         | ✔️     |       |      | ✔️     |
| [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage)        | Travis, setuptools, Tox    | git, manual    | 10      |         |        |       |      |        |
| [cookiecutter-pylibrary](https://github.com/ionelmc/cookiecutter-pylibrary)              | Travis, setuptools, Tox    | git, manual    | 20      |         |        |       |      | ✔      |
| [cookiecutter-django](https://github.com/pydanny/cookiecutter-django)                    | Actions, setuptools, Tox   | git, manual    | 15      |         | ✔️     |       |      | ✔️     |
| [django-init](https://github.com/Fueled/django-init)                                     | Actions, setuptools, Make  | git, manual    | 15      |         | ✔️     |       |      | ✔️     |
| [docker-science](https://github.com/docker-science/cookiecutter-docker-science)          | Make, Docker, setuptools   | no CI/CD       | 15      |         | ✔️     |       |      |        |
| [science-notebook-template](https://github.com/dmyersturnbull/science-notebook-template) | Conda                      | no CI/CD       | 5       |         | ✔️     |       |      | ✔️     |

**Notes:**

**† _N int._**: Approximate number of built-in integrations with tools and standards. What counts is very roughly defined.
**‡ _Modern_**: Lacks legacy files and tools. I’m including Make, setuptools, pipenv, and some others.
**Note:** [copier](https://github.com/copier-org/copier) syncs with a remote template. It’s a neat idea that Tyranno lacks.

Some of the packages in the table above need more explanation:

- [hypermodern-python](https://github.com/cjolowicz/hypermodern-python)
  ([template](https://github.com/cjolowicz/cookiecutter-hypermodern-python)), a Poetry-powered Python
  template. It’s good, but it made a few unusual choices, such as [Nox](https://github.com/theacodes/nox), which has <500 GitHub stars.
- Both [cookiecutter-django](https://github.com/pydanny/cookiecutter-django) and
  [django-init](https://github.com/Fueled/django-init) have fantastic setups for Django projects.
- [Cookiecutter-docker-science](https://github.com/docker-science/cookiecutter-docker-science) is an interesting project
  that doesn’t quite fit in this list.

### ✨ Projects made with Tyranno

These are some example projects that were generated with Tyranno:

- [Tyranno](https://github.com/dmyersturnbull/tyranno)
- [Realized](https://github.com/dmyersturnbull/realized)
- [SmartIo](https://github.com/dmyersturnbull/smartio)
- [typed-dfs](https://github.com/dmyersturnbull/typed-dfs)
- [suretime](https://github.com/dmyersturnbull/suretime)
- [auth_capture_proxy](https://github.com/alandtse/auth_capture_proxy)

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
