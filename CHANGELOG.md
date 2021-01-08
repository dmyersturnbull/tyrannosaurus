# Changelog

Adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
and [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
After v1.0, will follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).


## [0.8.x] - 2021-01-08

### Changed
- Moved build to Python 3.9 (internal only)
- Bumped and simplified a few dependencies
- Moved pre-commit run commands in tox to after poetry install, so versions are enforced
- Replaced flake8-bandit with `bandit -r .` call (the former is abandoned)
- Made compatible with Github’s [master branch renaming](https://github.com/github/renaming)
  (Because this external change broke backwards compatibility for newly generated projects,
  I consider this a fix, which won’t trigger a minor version bump)

### Added
- A `--track` flag in `tyrannosaurus new` (to simplify the readme’s example)
- Some currently unused items in [tool.tyrannosaurus.sources]
- Integration with [https://github.com/pyupio/safety](Safety)
- A `--tyranno` flag to new (deprecates `--newest`, which is now hidden)
- `--version` and `--info` options (exit immediately)
- Support for Github packages (technically should trigger a minor version bump)

### Removed
- isort, which conflicted with black anyway
- trailing-whitespace hook, which was unnecessary due to black and prettifier,
  and which incorrectly modified markdown files

### Fixed
- Cleaned up code
- Bad editorconfig settings for yaml and json
- Improved readme and docs
- Wrote better descriptions and names of workflows
- Missing 'feature' and 'security' labels in pull request templates
- Added `.mypy_cache` to the trash list


## [0.8.0] - 2020-08-28

### Changed
- Split pull and push workflows

### Fixed
- Coveralls integration
- Bug in which some paths weren’t deleted by `clean`


## [0.7.0] - 2020-08-26

### Removed
- Support for Python 3.7

### Fixed
- Use git tag for the current version for `tyrannosaurus new`
- Improved docs build
- Dropped unnecessary dependencies
- Unnecessary flake8 checks included for tests/


## [0.6.0] - 2020-08-05

### Changed
- Removed `poetry lock` from tox and added it to `tyrannosaurus sync`.
- Removed tests from the release workflow.
- Moved coveralls command from tox to the Github commit workflow.
- Bumped versions of pre-commit and poetry.

### Added
- A `tyrannosaurus build` command that does everything.
- JSON, YAML, and TOML checks to `tox.ini`.

### Fixed
- `tomlkit` needs to be 0.5.x (< 6) for Poetry compatibility.


## [0.5.x] - 2020-05-15

### Fixed
- `poetry.lock` was not deleted
- some files, including `__init__.py`, were ignored
- fixed options in `tox.ini`
- removed some stupid items in `pyproject.toml`
- proper handling of dashes and underscores
- git config was not used
- removed `.coverage` sqllite file
- simplified code by copying `pyproject.toml` to resources
- bumped CC-BY and CC-BY-NC to 4.0 (3.0 was by mistake)
- added tyrannosaurus to tox whitelist
- updated minor dependency versions
- a bug affecting Windows

### Changed
- Reorganized documentation files and added a little.

### Removed
- automatic installation of shell completions


## [0.5.0] - 2020-05-11

### Added
- `CITATION.cff` and `codemeta.json`
- `CONTRIBUTING.md` and issue and pull request templates
- Unfinished `update` command

### Changed
- The way authors, maintainers, and contributors are listed

### Fixed
- Split `cli.py` into multiple files


## [0.4.x] - 2020-05-09

### Fixed
- Incorrect processing of pip requirements in `env`
- Missing `path` argument to `env`


## [0.4.0] - 2020-05-09

### Added
- Tyrannosaurus commands to tox
- Upload sdist and wheel to release
- Workflow to release on tag

### Changed
- Python version for building to 3.8
- Renamed `reqs` to `info`

### Removed
- `check-added-large-files`, which is too slow

### Fixed
- The test workflow wasn’t testing
- A bug getting the `git config` when called with `new`


## [0.3.0] - 2020-05-08

### Added
- Command `env`


## [0.2.0] - 2020-05-08

### Added
- Commands `new`, `sync`, `recipe`, and `clean`

### Fixed
- Several minor build issues
- Documentation formatting


## [0.1.0] - 2020-05-05

### Added
- Github actions


## [0.0.3] - 2020-05-05

### Fixed
- Failing docs build.
- Renamed changelog to `CHANGELOG.md` and added structure.


## [0.0.2] - 2020-04-31

Completely different project with a different purpose.

### Changed
- Revamped build structure, removing `setup.py`.

### Added
- A `tox.ini` with a single entry point.

### Removed
- `metadata.py`. Use `__init__.py` instead.
- Various nonsense code


## [0.0.1] - 2020-04-02

### Added
Nonsense code and docs that were never used.
