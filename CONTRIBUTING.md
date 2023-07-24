# Contributing

<!-- :tyranno: ${project.name~|sentence(@)~} -->

# Tyranno

[Apache License, version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

New issues and pull requests are welcome.
Feel free to direct a question to the authors by submitting a
[_question_ issue](https://github.com/dmyersturnbull/tyranno/issues/new?template=question.md).
Contributors are asked to abide by the
[GitHub community guidelines](https://docs.github.com/en/site-policy/github-terms/github-community-guidelines)
and the [Contributor Code of Conduct, version 2.0](https://www.contributor-covenant.org/version/2/0/code_of_conduct/).

## Commit messages

Follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/),
the [Angular commit guidelines](https://github.com/angular/angular/blob/master/CONTRIBUTING.md),
and [Semantic Versioning 2](https://semver.org/spec/v2.0.0.html).
We follow the “Guiding Principles” of [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/)
but not the “Types of changes”, which contradict the Angular commit types.

Angular-style commit messages should get mapped to changelog sections and issue labels.
In this table, _BREAKING_ refers to the `BREAKING CHANGE` prefix in the commit body.
We note that bug fixes are always technically breaking changes because callers can depend on the incorrect behavior.
We allow most to trigger minor version bumps. and do not require the _BREAKING_ label.

| Commit keyword | Section              | semver      | issue label(s)      |
| -------------- | -------------------- | ----------- | ------------------- |
| `!`            | `⚠ BREAKING CHANGES` | major       | `breaking`          |
| none           | `🔒 Security`        | N/A         | `security`          |
| none           | `✨ Highlight`       | N/A         | `highlight`         |
| `feat:`        | `✨ Features`        | minor       | `type: feature`     |
| `fix:`         | `🐛 Bug fixes`       | minor       | `type: fix`         |
| `docs:`        | `📝 Documentation`   | patch       | `type: docs`        |
| `build:`       | `🛠 Build System`     | minor/patch | `type: build`       |
| `perf:`        | `🚀 Performance`     | patch       | `type: performance` |
| `test:`        | `🚨 Tests`           | none        | `type: test`        |
| `style:`       | none                 | none        | none                |
| `chore:`       | none                 | none        | none                |
| `refactor:`    | none                 | none        | none                |
| `ci:`          | none                 | none        | none                |
| `revert:`      | none                 | none        | none                |

## Pull requests

Please update `CHANGELOG.md` and add your name to the contributors in `pyproject.toml` so that you’re credited.
Then make a draft pull request and solicit feedback.

## Publishing a new version

1. On the _main_ branch, run `cz bump`.
2. Wait a few minutes, then pull the main branch back.
3. Run, e.g., `git tag -s v1.13.2` (note the `v`). Push the tag.
   20 minutes later, verify that the _deploy_ workflow completed successfully.
4. Copy `recipes/` to the [feedstock](https://github.com/conda-forge/tyranno-feedstock).
   20 minutes later, verify that the Conda-Forge shield updated.

## Versioning

Versioning is a subset of [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
Git tags and GitHub releases are prefixed with `v` (e.g. `v0.1.1`).

- Stable releases MUST use: `major "." minor "." patch ["+" platform]`.
- Pre-alpha releases MUST use: `major "." minor "." patch "-" build "+" [platform "."]`,
  where `build` increments per tag starting at _0_.
- Alpha, beta, and RC releases, if used, increment per tag starting at 1 (e.g. `alpha1`).
  Alpha/beta/RC MUST NOT be used out of order (e.g. **not** `alpha1`, `beta1`, `alpha2`).
  If major version > 0, releases lacking a build tag SHOULD be preceded by at least one alpha, beta, or RC release.
- If major version = 0, unstable releases MAY include a build tag.

## Conventions

### Filesystem, URL, URI, and IRI node naming

See [Google’s filename conventions](https://developers.google.com/style/filenames).
Prefer kebab-case with one or more filename extensions: `[a-z0-9-]+(\.[a-z0-9]+)+`.
Always use a filename extension, and prefer `.yaml` for YAML and `.html` for HTML.
If necessary, `,`, `+`, and `~` can be used as word separators with reserved meanings.
Always use `/` as a path separator in documentation.

### Python classes

Use [pydantic](https://pydantic-docs.helpmanual.io/) or
[dataclasses](https://docs.python.org/3/library/dataclasses.html).
Use immutable typesunless there’s a compelling reason otherwise.

#### With pydantic

```python
import orjson
from pydantic import BaseModel


def to_json(v) -> str:
    return orjson.dumps(v).decode(encoding="utf8")


def from_json(v: str):
    return orjson.loads(v).encode(encoding="utf8")


class Cat(BaseModel):
    breed: str | None
    age: int
    names: frozenset[str]

    class Config:
        frozen = True
        json_loads = from_json
        json_dumps = to_json
```

#### With dataclasses

Use, wherever possible: `slots=True, frozen=True, order=True`
Use `KW_ONLY` in favor of `kwonly=True` (for consistency).

```python
import orjson
from dataclasses import dataclass, KW_ONLY


def to_json(v) -> str:
    return orjson.dumps(v).decode(encoding="utf8")


def from_json(v: str):
    return orjson.loads(v).encode(encoding="utf8")


@dataclass(slots=True, frozen=True, order=True)
class Cat:
    breed: str | None
    age: int
    _: KW_ONLY
    names: frozenset[str]

    def json(self) -> str:
        return to_json(self)
```
