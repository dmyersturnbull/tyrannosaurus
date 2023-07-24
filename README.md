# Tyranno

<!--<< :tyranno: [![Version status](https://img.shields.io/pypi/status/${project.name}?label=Status)](https://pypi.org/project/${project.name}) -->

[![Version status](https://img.shields.io/pypi/status/tyranno?label=Status)](https://pypi.org/project/tyranno)

<!--<< :tyranno: [![Version on PyPi](https://badgen.net/pypi/v/${project.name}?label=PyPi -->

[![Version on PyPi](https://badgen.net/pypi/v/tyranno?label=PyPi)](https://pypi.org/project/tyranno)

<!--<< :tyranno: [![Version on GitHub](https://badgen.net/github/release/${.frag}/stable?label=GitHub)](${project.urls.repo}/releases) -->

[![Version on GitHub](https://badgen.net/github/release/dmyersturnbull/tyranno/stable?label=GitHub)](https://github.com/dmyersturnbull/tyranno/releases)

<!--<< :tyranno: [![Version on Docker Hub](https://img.shields.io/docker/v/dmyersturnbull/tyranno?color=green&label=Docker%20Hub)](https://hub.docker.com/repository/docker/${.frag}) -->

[![Version on Docker Hub](https://img.shields.io/docker/v/dmyersturnbull/tyranno?color=green&label=Docker%20Hub)](https://hub.docker.com/repository/docker/dmyersturnbull/tyranno)

<!--<< :tyranno: [![Version on Conda-Forge](https://img.shields.io/conda/vn/conda-forge/${project.name}?label=Conda-Forge)](https://anaconda.org/conda-forge/${project.name})\ -->

[![Version on Conda-Forge](https://img.shields.io/conda/vn/conda-forge/tyranno?label=Conda-Forge)](https://anaconda.org/conda-forge/tyranno)

[![Build (Actions)](https://img.shields.io/github/workflow/status/dmyersturnbull/tyranno/maintest?label=Tests)](https://github.com/dmyersturnbull/tyranno/actions)

<!--<< :tyranno: [![Documentation status](${project.urls.docs}/badge)]($project.urls.docs}) -->

[![Documentation status](https://readthedocs.org/projects/tyranno/badge)](https://tyranno.readthedocs.io/en/stable/)

<!--<< :tyranno: [![Coverage (coveralls)](https://badgen.net/coveralls/c/github/${project.name}/${project.name}?label=Coveralls)](https://coveralls.io/github/${.frag}?branch=main) -->

[![Coverage (coveralls)](https://badgen.net/coveralls/c/github/dmyersturnbull/tyranno?label=Coveralls)](https://coveralls.io/github/dmyersturnbull/tyranno?branch=main)

<!--<< :tyranno: [![Coverage (codecov)](https://badgen.net/codecov/c/github/${.frag}?label=CodeCov)](https://codecov.io/gh/${.frag})\ -->

[![Coverage (codecov)](https://badgen.net/codecov/c/github/dmyersturnbull/tyranno?label=CodeCov)](https://codecov.io/gh/dmyersturnbull/tyranno)

<!--<< :tyranno: [![Maintainability (Code Climate)](https://badgen.net/codeclimate/maintainability/${.frag})](https://codeclimate.com/github/${.frag}/maintainability) -->

[![Maintainability (Code Climate)](https://badgen.net/codeclimate/maintainability/dmyersturnbull/tyranno)](https://codeclimate.com/github/dmyersturnbull/tyranno/maintainability)

<!--<< :tyranno: [![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/${.frag}/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/${.frag}/?branch=main) -->

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/dmyersturnbull/tyranno/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/dmyersturnbull/tyranno/?branch=main)

<!--<< :tyranno: [![CodeFactor](https://www.codefactor.io/repository/github/${.frag}/badge)](https://www.codefactor.io/repository/github/${.frag}) -->

[![CodeFactor](https://www.codefactor.io/repository/github/dmyersturnbull/tyranno/badge)](https://www.codefactor.io/repository/github/dmyersturnbull/tyranno)

<!--<< :tyranno: [![License](https://badgen.net/pypi/license/${project.name}?label=License)](${.license.url}) -->

[![License](https://badgen.net/pypi/license/tyranno?label=License)](https://opensource.org/licenses/Apache-2.0)

<!--<< :tyranno: [![DOI](https://zenodo.org/badge/DOI/${.doi}.svg)](https://doi.org/${.doi}) -->

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4485186.svg)](https://doi.org/10.5281/zenodo.4485186)

<!--<< :tyranno: [![Created with ${project.name}](https://img.shields.io/badge/Created_with-${project.name}-0000ff.svg)](https://github.com/${.frag}) -->

[![Created with Tyranno](https://img.shields.io/badge/Created_with-Tyranno-0000ff.svg)](https://github.com/dmyersturnbull/tyranno)

Tyranno is a highly streamlined modern Python template
backed by [Hatch](https://hatch.pypa.io/), pre-commit, commitizen, static analysis tools, and GitHub Actions.
Automagically works with Docker, container registries, Conda, readthedocs, GitHub Pages.
Optionally add `:tyranno:` comments to sync project metadata like versions every time you commit.

The focus is on automation and modern tooling.
Clone this repo to get started. Installing [Probot settings](https://github.com/probot/settings) is also recommended.

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

## 🎁 Features & integrations

- Packaging and dependency management with [Poetry](https://python-poetry.org/)
- Python 3.7 thru 3.12
- Only modern files: _no_ manifest file, setup.py, requirements.txt, setup.cfg, or eggs
- Continuous integration with [GitHub Actions](https://github.com/features/actions)
- Continuous deployment to [PyPi](http://pypi.org/) and [Docker Hub](https://hub.docker.com/).
- Deployment to the [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry);
  plus to any other desired container registries with a simple modification.
- Automatic attachment of [sdits](https://docs.python.org/3/distutils/sourcedist.html)
  and [wheels](https://pythonwheels.com/) to
  [GitHub Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
- Good default GitHub settings, synchronized via [Probot settings](https://github.com/probot/settings)
- Documentation sent to [readthedocs](https://readthedocs.org/)
- Nice documentation defaults via CommonMark and
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
  [Prettifier](https://prettier.io/),
  and [markdown-lint-check](https://github.com/gaurav-nelson/github-action-markdown-link-check)
- Security analysis with [Bandit](https://github.com/PyCQA/bandit),
  [CodeQL](https://github.com/github/codeql-action),
  and [safety](https://github.com/pyupio/safety)
- Static type analysis with [mypy](https://mypy.readthedocs.io)
- [Conda-Forge](https://conda-forge.org/) [recipes](https://conda-forge.org/docs/maintainer/adding_pkgs.html#the-recipe-meta-yaml)
  and [environment YML](https://medium.com/@balance1150/how-to-build-a-conda-environment-through-a-yaml-file-db185acf5d22)
  with [Grayskull](https://github.com/conda-incubator/grayskull)
- IDE hints via [EditorConfig](https://editorconfig.org/) with good defaults for most languages
- Fancy issue labels
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

[x] An **elegant CI/CD workflow**: Workflows are kicked off only by `git push`.
[x] **Interoperability with Conda**, including recipes and environment files, by mapping dependencies and metadata.
[x] **Automated publishing** to PyPi, Conda-Forge, Docker Hub, the GitHub Container Registry, and readthedocs.
[x] **No duplication** between project files.
[x] Complete **absence of legacy tools**, files, and Python 2 support.

### 🏁 Feature table

| Tool                                                                                     | Main techs                 | CD kickoff     | N int.† | modern‡ | Docker | Conda | sync | any-OS |
| ---------------------------------------------------------------------------------------- | -------------------------- | -------------- | ------- | ------- | ------ | ----- | ---- | ------ |
| Tyranno                                                                                  | Actions, Hatch             | git, GitHub    | 25      | ✔️      | ✔️     | ✔️    | ✔️   | ✔️     |
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
