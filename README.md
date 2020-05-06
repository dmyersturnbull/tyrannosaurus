# Tyrannosaurus Reqs

[![Build status](https://img.shields.io/pypi/status/tyrannosaurus)](https://pypi.org/project/tyrannosaurus/)
[![Latest version on PyPi](https://badge.fury.io/py/tyrannosaurus.svg)](https://pypi.org/project/tyrannosaurus/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/tyrannosaurus.svg)](https://pypi.org/project/tyrannosaurus/)
[![Documentation status](https://readthedocs.org/projects/tyrannosaurus/badge/?version=latest&style=flat-square)](https://readthedocs.org/projects/tyrannosaurus/)
[![Travis](https://travis-ci.org/dmyersturnbull/tyrannosaurus.svg?branch=master)](https://travis-ci.org/dmyersturnbull/tyrannosaurus)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

An opinionated 2020 Python template.
Just clone it and modify or run `tyrannosaurus new`.

⚠ Status: Under development. The template works, but the command-line tool doesn't.

[Poetry](https://github.com/python-poetry/poetry) is fantastic and assumed.
New projects are configured for:
- Build: [Poetry](https://github.com/python-poetry/poetry), Tox, Conda, [DepHell](https://github.com/dephell/dephell), wheels, sdist
- Test: Travis, Tox, pytest, Coverage
- Style: Black, Flake8, MyPy, pycodestyle, pydocstyle
- Hooks: [EditorConfig](https://editorconfig.org/), pre-commit-hooks
- Documentation: ReadTheDocs, Sphinx, sphinx-autoapi
- Publish: Twine, Docker, Conda-Forge (with [grayskull](https://github.com/marcelotrevisani/grayskull))


### Synchronize repeated metadata

Provides `tyrannosaurus sync` to copy metadata from your `pyproject.toml` other config files.
The information copied includes version, description, dependencies, maintainers, and style settings.
You can configure these under `[tool.tyrannosaurus.sources]` and `[tool.tyrannosaurus.targets]`.
Always generates backups before modifying.

Here are most of the available synchronization targets:
- Copyright, status, and date in `__init__.py`
- Development dependencies between `tool.poetry.dev-dependencies`, `tool.poetry.extras`, and `tox.ini`
- An `all` optional dependency list with all optional non-dev packages
- Dependencies for building docs in `docs/conf.py`
- Code line length between `isort`, `black`, and `pycodestyle`
- Python version in `pyproject.toml`, `tox.ini`, `.travis.yml`, `black`, and `readthedocs.yml`
- Copyright in `docs/conf.py`
- Poetry version in `Dockerfile`
- Authors and year listed in the license file
- Dev versions in `.pre-commit-config.yaml`
- `--maintainers` arg for Grayskull in `tox.ini`
- `doc_url`, `dev_url`, and `license_file` in `meta.yaml`
- Most recent version in `CHANGELOG.md` assuming [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

### Reference of commands

Here are some useful commands:
- `pre-commit install` to configure pre-commit hooks
- `tox` to sync metadata, build, install, build docs, and test
- `poetry install` to install and nothing more
- `poetry build` to build wheels and sdists and nothing more
- `poetry bump` to bump dependency versions (major or minor)
- `poetry publish` to upload to PyPi
- `grayskull ${yourprojectname} --maintainers $(git config user.email) --output recipes/` to generate a Conda recipe
- `tyrannosaurus sync` to sync metadata and nothing else
- `tyrannosaurus clean --aggressive` to remove lots of temp files

### Other things to set up
- More pre-commit-config options, such as `check-yaml`
- GPG keys with git: `git config --global user.signingkey`
- GPG keys with Twine: use `twine -s`
- A certificate with [Certbot](https://certbot.eff.org/) if you need one
- Github labels, such as [Tyrannosaurus's labels](https://github.com/dmyersturnbull/tyrannosaurus/labels)

### Uploading to Conda-Forge

To [upload a package to Conda-Forge](https://conda-forge.org/#add_recipe):
1. Publish to PyPi, then run `grayskull` as above and then `tyrannosaurus sync`.
2. Check over your new recipe in `recipes/projectname/meta.yaml`.
3. Fork from [staged-recipes](https://github.com/conda-forge/staged-recipes).
4. Copy your recipe from `recipes/projectname/meta.yaml` into the forked repo (keeping the directories).
5. Make a pull request. If everything goes well, it will be on Conda-Forge soon!

### Suggested standards to observe

Here are some potentially useful standards:
- [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
- [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) recommendations.
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).
- According to taste, only Git rebase (never merge)


### Building, extending, and contributing

[New issues](https://github.com/dmyersturnbull/tyrannosaurus/issues) and pull requests are welcome.

Tyrannosaurus is licensed under the [Apache License, version 2.0](https://www.apache.org/licenses/LICENSE-2.0).
The author wrote it after making 18 Git commits trying to configure readthedocs, PyPi, and Tox.
This avoids that struggle for 99% of projects.



```
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
