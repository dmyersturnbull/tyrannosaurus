# Changelog

Adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
and [keep a Changelog](https://keepachangelog.com/en/1.0.0/).
After v1.0, will follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

Commit messages should get mapped to changelog sections this way:

| Commit prefix | Section   | semver |
| ------------- | --------- | ------ |
| `breaking:`   | `Changed` | major  |
| `feat:`       | `Added`   | minor  |
| `docs:`       | `Fixed`   | patch  |
| `fix:`        | `Fixed`   | patch  |
| `refactor:`   | `Fixed`   | patch  |
| `test:`       | `Fixed`   | patch  |
| `chore:`      | `Fixed`   | patch  |
| `style:`      | skipped   | never  |

## [0.10.0] - unreleased

## [0.9.x] - 2021-01-31

### Added

- A code of conduct
- More pre-commit hooks (esp. prettier and nbstripout)

### Changed

- Improved the contributing guide

### Fixed

- Added missing settings.yml file

## [0.9.0] - 2021-01-31

### Added

- A [probot](https://github.com/probot/settings) config file _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- [Commitizen](https://github.com/commitizen-tools/commitizen) config
- A Vagrant stub file _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- A feature comparison table _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Colors to the CLI
- Slack notifications and `actions-options.json`

### Changed

- Template params now start with `$${` to avoid conflicts _―[dmyersturnbull](https://github.com/dmyersturnbull)_

### Removed

- Install dev extras in tox; they're installed in poetry _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- The deprecated `--latest` flag

### Fixed

- Improved the new-project guide _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- A few misc bugs _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Dockerfile labels and lint passing
- Verbose and dry-run options

## [0.8.x] - 2021-01-08

### Added

- A `--track` flag in `tyrannosaurus new` (to simplify the readme’s example) _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Some currently unused items in [tool.tyrannosaurus.sources] _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Integration with [Safety](https://github.com/pyupio/safety) _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- A `--tyranno` flag to new (deprecates `--newest`, which is now hidden) _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- `--version` and `--info` options (exit immediately) _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Support for Github packages (technically should trigger a minor version bump) _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Stub and shields for scrutinizer _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Source license headers _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Link to license in default readme _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Real conda-forge recipe and shield for it _―[dmyersturnbull](https://github.com/dmyersturnbull)_

### Changed

- Moved build to Python 3.9 (internal only) _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Bumped and simplified a few dependencies _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Moved pre-commit run commands in tox to after poetry install, so versions are enforced _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Replaced flake8-bandit with `bandit -r .` call (the former is abandoned) _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Made compatible with Github’s [master branch renaming](https://github.com/github/renaming) _―[dmyersturnbull](https://github.com/dmyersturnbull)_
  (Because this external change broke backwards compatibility for newly generated projects,
  I consider this a fix, which won’t trigger a minor version bump)

### Deprecated

- `--newest` flag

### Removed

- isort, which conflicted with black anyway _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- trailing-whitespace hook, which was unnecessary due to black and prettifier, _―[dmyersturnbull](https://github.com/dmyersturnbull)_
  and which incorrectly modified markdown files

### Fixed

- Cleaned up code _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Bad editorconfig settings for yaml and json _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Improved readme and docs _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Wrote better descriptions and names of workflows _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Missing 'feature' and 'security' labels in pull request templates _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Added `.mypy_cache` to the trash list _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- `ccybync` instead of `ccbync` _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Incorrectly recognized license files _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Added `.git` to `.dockerignore`, and `*.tgz` and `!.npmignore` to `.gitignore` _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Generated recipes, including Poetry, Python version, and URLs _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- `tyrannosaurus recipe` won’t fail on a non-empty directory _―[dmyersturnbull](https://github.com/dmyersturnbull)_

## [0.8.0] - 2020-08-28

### Changed

- Split pull and push workflows _―[dmyersturnbull](https://github.com/dmyersturnbull)_

### Fixed

- Coveralls integration _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Bug in which some paths weren’t deleted by `clean` _―[dmyersturnbull](https://github.com/dmyersturnbull)_

## [0.7.0] - 2020-08-26

### Removed

- Support for Python 3.7 _―[dmyersturnbull](https://github.com/dmyersturnbull)_

### Fixed

- Use git tag for the current version for `tyrannosaurus new` _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Improved docs build _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Dropped unnecessary dependencies _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Unnecessary flake8 checks included for tests/ _―[dmyersturnbull](https://github.com/dmyersturnbull)_

## [0.6.0] - 2020-08-05

### Added

- A `tyrannosaurus build` command that does everything. _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- JSON, YAML, and TOML checks to `tox.ini`. _―[dmyersturnbull](https://github.com/dmyersturnbull)_

### Changed

- Removed `poetry lock` from tox and added it to `tyrannosaurus sync`. _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Removed tests from the release workflow. _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Moved coveralls command from tox to the Github commit workflow. _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Bumped versions of pre-commit and poetry. _―[dmyersturnbull](https://github.com/dmyersturnbull)_

### Fixed

- `tomlkit` needs to be 0.5.x (< 6) for Poetry compatibility. _―[dmyersturnbull](https://github.com/dmyersturnbull)_

## [0.5.x] - 2020-05-15

### Changed

- Reorganized documentation files and added a little. _―[dmyersturnbull](https://github.com/dmyersturnbull)_

### Removed

- automatic installation of shell completions _―[dmyersturnbull](https://github.com/dmyersturnbull)_

### Fixed

- `poetry.lock` was not deleted _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- some files, including `__init__.py`, were ignored _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- fixed options in `tox.ini` _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- removed some stupid items in `pyproject.toml` _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- proper handling of dashes and underscores _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- git config was not used _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- removed `.coverage` sqllite file _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- simplified code by copying `pyproject.toml` to resources _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- bumped CC-BY and CC-BY-NC to 4.0 (3.0 was by mistake) _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- added tyrannosaurus to tox whitelist _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- updated minor dependency versions _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- a bug affecting Windows _―[dmyersturnbull](https://github.com/dmyersturnbull)_

## [0.5.0] - 2020-05-11

### Added

- `CITATION.cff` and `codemeta.json` _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- `CONTRIBUTING.md` and issue and pull request templates _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Unfinished `update` command _―[dmyersturnbull](https://github.com/dmyersturnbull)_

### Changed

- The way authors, maintainers, and contributors are listed _―[dmyersturnbull](https://github.com/dmyersturnbull)_

### Fixed

- Split `cli.py` into multiple files _―[dmyersturnbull](https://github.com/dmyersturnbull)_

## [0.4.x] - 2020-05-09

### Fixed

- Incorrect processing of pip requirements in `env` _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Missing `path` argument to `env` _―[dmyersturnbull](https://github.com/dmyersturnbull)_

## [0.4.0] - 2020-05-09

### Added

- Tyrannosaurus commands to tox _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Upload sdist and wheel to release _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Workflow to release on tag _―[dmyersturnbull](https://github.com/dmyersturnbull)_

### Changed

- Python version for building to 3.8 _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Renamed `reqs` to `info` _―[dmyersturnbull](https://github.com/dmyersturnbull)_

### Removed

- `check-added-large-files`, which is too slow _―[dmyersturnbull](https://github.com/dmyersturnbull)_

### Fixed

- The test workflow wasn’t testing _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- A bug getting the `git config` when called with `new` _―[dmyersturnbull](https://github.com/dmyersturnbull)_

## [0.3.0] - 2020-05-08

### Added

- Command `env` _―[dmyersturnbull](https://github.com/dmyersturnbull)_

## [0.2.0] - 2020-05-08

### Added

- Commands `new`, `sync`, `recipe`, and `clean` _―[dmyersturnbull](https://github.com/dmyersturnbull)_

### Fixed

- Several minor build issues _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Documentation formatting _―[dmyersturnbull](https://github.com/dmyersturnbull)_

## [0.1.0] - 2020-05-05

### Added

- Github actions _―[dmyersturnbull](https://github.com/dmyersturnbull)_

## [0.0.3] - 2020-05-05

### Fixed

- Failing docs build _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Renamed changelog to `CHANGELOG.md` and added structure. _―[dmyersturnbull](https://github.com/dmyersturnbull)_

## [0.0.2] - 2020-04-31

Completely different project with a different purpose.

### Added

- A `tox.ini` with a single entry point. _―[dmyersturnbull](https://github.com/dmyersturnbull)_

### Changed

- Revamped build structure, removing `setup.py`. _―[dmyersturnbull](https://github.com/dmyersturnbull)_

### Removed

- `metadata.py`. Use `__init__.py` instead. _―[dmyersturnbull](https://github.com/dmyersturnbull)_
- Various nonsense code _―[dmyersturnbull](https://github.com/dmyersturnbull)_

## [0.0.1] - 2020-04-02

### Added

- Nonsense code and docs that were never used. _―[dmyersturnbull](https://github.com/dmyersturnbull)_
