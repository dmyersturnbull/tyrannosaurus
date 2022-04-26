# Contributing

Tyrannosaurus is licensed under the
[Apache License, version 2.0](https://www.apache.org/licenses/LICENSE-2.0).
New issues and pull requests are welcome.
Feel free to direct a question to the authors by creating an
[issue with the _question_ tag](https://github.com/dmyersturnbull/tyrannosaurus/issues/new?assignees=&labels=kind%3A+question&template=question.md).
Contributors are asked to abide by both the
[GitHub community guidelines](https://docs.github.com/en/github/site-policy/github-community-guidelines)
and the [Contributor Code of Conduct, version 2.0](https://www.contributor-covenant.org/version/2/0/code_of_conduct/).

### Commit messages

Don’t worry about this too much.
Follows [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
and the [Angular commit guidelines](https://github.com/angular/angular/blob/master/CONTRIBUTING.md),
along with [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
and [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

Angular-style commit messages should get mapped to changelog sections and issue labels.
In this table, _Breaking_ refers to the `BREAKING CHANGE` prefix in the commit body (2nd section).
_Refactor_ can get mapped differently depending on whether any public API is changed or removed.
Some commits can trigger multiple changelog items (e.g. under both _Changed_ and _Removed_).
We deviate slightly from semantic versioning by allowing some essentially non-breaking bug fixes to
trigger minor version bumps. This could be, for example, a thrown exception or incorrect return
value a caller could reasonably depend on the incorrect behavior.

| Commit prefix   | Section   | semver | issue label(s)             |
| --------------- | --------- | ------ | -------------------------- |
| Breaking (body) | N/A       | major  | breaking                   |
| `feat:`         | `Added`   | minor  | new feature or enhancement |
| `docs:`         | `Fixed`   | patch  | documentation              |
| `fix:` (1)      | `Fixed`   | patch  | bug                        |
| `fix:` (2)      | `Fixed`   | minor  | bug                        |
| `refactor:` (1) | `Changed` | major  | cleanup and/or enhancement |
| `refactor:` (2) | `Removed` | major  | cleanup and/or enhancement |
| `refactor:` (3) | ignored   | patch  | cleanup                    |
| `build:`        | `Fixed`   | patch  | infrastructure             |
| `test:`         | ignored   | patch  | tests                      |
| `ci:`           | ignored   | never  | infrastructure             |
| `style:`        | ignored   | never  | cleanup                    |

### Pull requests

Please update `CHANGELOG.md` and add your name to the contributors in `pyproject.toml`
so that you’re credited. Run `poetry lock` and `tyrannosaurus sync` to sync metadata.
Feel free to make a draft pull request and solicit feedback from the authors.

### Publishing a new version

1. Bump the version in `tool.poetry.version` in `pyproject.toml`, following the rules described below.
2. Run `tyrannosaurus sync` so that the Poetry lock file is up-to-date
   and metadata are synced to pyproject.toml.
3. Create a [new release](https://github.com/dmyersturnbull/tyrannosaurus/releases/new)
   with both the name and tag set to something like `v1.4.13` (keep the _v_).
4. An hour later, check that the _publish on release creation_
   [workflow](https://github.com/dmyersturnbull/tyrannosaurus/actions) passes
   and that the PyPi, Docker Hub, and GitHub Package versions are updated as shown in the
   shields on the readme.
5. Check for a pull request from regro-cf-autotick-bot on the
   [feedstock](https://github.com/conda-forge/tyrannosaurus-feedstock).
   _If you have not changed the dependencies or version ranges_, go ahead and merge it.
   Otherwise, [update the recipe](https://github.com/conda-forge/tyrannosaurus-feedstock/edit/master/recipe/meta.yaml)
   with those changes under `run:`, also updating `{% set version` and `sha256` with the
   changes from regro-cf-autotick-bot. You can alternatively re-run `tyrannosaurus recipe`
   to generate a new recipe and copy it to the feedstock.
6. Twenty minutes later, verify that the Conda-Forge shield is updated.

#### Versioning

Versioning is a subset of [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
Git tags and GitHub releases use this notation, prefixed with `v` (e.g. `v0.1.1`).

- Stable releases MUST use: `major "." minor "." patch ["+" platform]`.
- Pre-alpha releases MUST use: `major "." minor "." patch "-" build "+" [platform "."]`,
  where `build` increments per tag starting at _0_.
- Alpha, beta, and RC releases, if used, increment per tag starting at 1 (e.g. `alpha1`).
  Alpha/beta/RC MUST NOT be used out of order (e.g. NOT `alpha1`, `beta1`, `alpha2`).
  If major version > 0, releases lacking a build tag SHOULD be preceded by at least one
  alpha, beta, or RC release.
- If major version = 0, unstable releases MAY include a build tag.

**In EBNF:**

```
version    = major , "." , minor , "." , patch , ["-" , build] , ["+" , platform] ;
major      = number ;
minor      = number ;
patch      = number ;
build      = number | (("alpha" | "beta" | "rc") , positive) ;
platform   = os | arch | (os , "." , arch) ;
os         = tag ;
arch       = tag ;

-- where (with regex):
tag        = [a-z]+ [a-z0-9]+
positive   = [1-9]  [0-9]+
number     = [0-9]+
```

**Illustration – example release history:**

1. `0.1.0`
2. `0.1.1`
3. `0.2.0-0 +1ca8da40`
4. `0.2.0-1 +f1c045ae`
5. `0.2.0`
6. `1.0.0-0 +10f011ca`
7. `0.2.1`
8. `1.0.0-rc1+aa40c1cf`
9. `1.0.0 +win11.1ca8da40`
