# Tyrannosaurus

[![Build status](https://img.shields.io/pypi/status/tyrannosaurus)](https://pypi.org/project/tyrannosaurus/)
[![Latest version on PyPi](https://badge.fury.io/py/tyrannosaurus.svg)](https://pypi.org/project/tyrannosaurus/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/tyrannosaurus.svg)](https://pypi.org/project/tyrannosaurus/)
[![Documentation status](https://readthedocs.org/projects/tyrannosaurus/badge/?version=latest&style=flat-square)](https://readthedocs.org/projects/tyrannosaurus/)
[![Travis](https://travis-ci.org/dmyersturnbull/tyrannosaurus.svg?branch=master)](https://travis-ci.org/dmyersturnbull/tyrannosaurus)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Coverage Status](https://coveralls.io/repos/github/dmyersturnbull/tyrannosaurus/badge.svg?branch=master)](https://coveralls.io/github/dmyersturnbull/tyrannosaurus?branch=master)

#### What it does:
- Generates Python projects configured for modern build tools and ready to upload to readthedocs, PyPi, and [Conda-Forge](https://conda-forge.org/).
- Synchronizes dependencies in setup.py, setup.cfg, requirements files, conda recipes, conda envs, pipenvs, and [poetry](https://python-poetry.org/) configs.
- Synchronizes poetry, pipenv, setuptools, and Conda information about your package, including description, version, license, etc.
- Lets your package’s users build with the tools they prefer.

#### What it doesn’t do:
- Resolve dependencies. See Poetry or Anaconda for this!
- Introduce a new path to list dependencies.

#### How to use it:

1. Install with `pip install tyrannosaurus`.
2. Create a project with `tyrannosaurus new`. Modify as you see fit.
4. Use `tyrannosaurus reqs` to synchronize your dependencies and project info (version number, description).
5. Optionally, run `tyrannosaurus reqs --latest`. This interfaces with Poetry and Conda-Forge to find package updates.

#### Conflict identification:

Poetry and Conda (and pipenv) are full dependency managers capable of identifying and resolving conflicts.
Tyrannosaurus is just smart enough to tell you when versions from Conda and PyPi cannot match.

#### ⚠ Status:

Not finished yet! The scripts are scattered everywhere. This should be ready in late April.

## Creating a new project

```
tyrannosaurus new mynewproject
```

Your new project is ready for PyPi, Sphinx, Sphinx API docs, readthedocs, Git, Tox, Travis, CircleCI, and conda-forge.
The Tox config will generate PyPi-ready source and wheel builds, and even a conda package for you!
Your project’s version is specified only once, in `yourpackage/__init__.py`.

You can modify your project freely after, and tyrannosaurus will still understand it.
Of course, `new` also has some command-line options. Run `tyrannosaurus new --help` to see them.
You can choose another license with `tyrannosaurus init mynewproject --license "MIT"`.

## Managing dependencies

Tyrannosaurus’s best feature is managing and translating dependencies.

#### Synchronizing dependencies:

It keeps your dependencies consistent between requirements.txt, conda recipes, Anaconda environment files, Pipfiles (pipenv), and setup.py files.
If there is a merge conflict, it will keep the highest version.
Just run:

```
tyrannosaurus reqs
```
No pun intended, of course.

#### Finding new versions on repositories

You can also update the versions to the most recent available on PyPi and your Anaconda channels:
It will report inconsistencies between Anaconda channel versions and versions on PyPi.

```
tyrannosaurus reqs --latest
```

#### Preferred version ranges:

By default, tyrannosaurus will use choose version ranges corresponding to the latest major version
The rationale is that compatibility with any minor version is guaranteed but compatibility with a new major version is not.
For example, if `5.8.2` is the latest, it will choose `>=5.8,<6.0`.
A good package manager will choose `5.8.2` over `5.8` if it can, but would of course reject `4.0` and `6.0`
This behavior can be configured (see below).
Note that this is the normal behavior of Poetry.

#### Finding dependencies from imports:

You can also use [pipreqs](https://github.com/bndr/pipreqs) to find dependencies from your imports.
This will find packages for your imports, assume the latest versions, verify, and add them to your lists.

```
tyrannosaurus reqs --find
```

#### Handling dependency conflicts:

All of these commands will tell you about dependency conflicts through Anaconda and/or Poetry, unless neither are installed.
If you only want to find conflicts and mismatches between your lists, call `tyrannosaurus check`.
This will also use `setup.py check` to verify that the `setup.py` is valid.
And of course, it will complain if it detects errors with other files.


## The project skeleton

When you run `tyrannosaurus new`, you’ll get a project structure that looks a lot like Tyrannosaurus’ own.
Just delete any config files you don’t want.

The initial structure was designed to keep configurable metadata in `metadata.py`.
The major advantage is that code can get this information without resorting to any trickery.
For example, you can print an up-to-date usage string with:

```python
from tyrannosaurus.metadata import Info
print(
    "{} version {} <{}>, copyright {}."
    .format(Info.name, Info.version, Info.url, Info.copyright)
)
```

The `setup.py` simply references these and shouldn’t need to be changed.
(You _can_ delete `metadata.py`, but you’ll need to remove references in `setup.py`—unless you also remove that file.)

You should not load external packages in either `metadata.py` or `setup.py`, since they won’t necessarily be installed.
Also note that tyrannosaurus actually executes `metadata.py`, so it shouldn’t have side effects.
If you rename `metadata.py`, just mention that it in `.tyrannosaurus`.

The most important metadata items are `name`, `description`, `release`, `version`, `license`, and `url`,
though several others are referenced in `setup.py`.
Tyrannosaurus will also pull the data from `pyproject.toml`, but not from `setup.py`.
(The reason is that it wants to avoid executing `setup.py`.)

Tyrannosaurus stores the previous values under `.tyrannosaurus-cache`
to detect changes. You may choose to check this into version control.
The default `.gitignore` has it whitelisted.
If it doesn’t have this cache (for example, if you just cloned the repository),
tyrannosaurus will simply list differences for you to change, and build its cache.

You’ll also notice that the default `setup.py` reads your `requirements.txt`.
This just saves some lines.
If you remove those lines with simple `install_requires` and `extras_requires` definitions,
then `tyrannosaurus reqs` will happily synchronize them and add manually defined entries.


### More about dependency translation

#### Optional dependencies:

You can distinguish between requirements and optional dependencies.
For example, your requirements.txt might look like this:
```
click                  >=7.1,<8.0
hypothesis[test]       >=5.8,<6.0
pytest[test]           >=5.4,<6.0
```

In `setup.py`, these are listed in `extras_require`.
Unfortunately, `environment.yml` files don’t support optional dependencies.
We get around this using comments starting with `# @`. See the docs for more info.

#### Python versions, and test and dev dependencies:

A few dependency categories are treated specially:
- _dev_, used by poetry and tox
- _test_, used by setuptools and poetry
- _python_, specifically python versions, required by setuptools, poetry, tox, pipenv, and conda

The syncing works the way you might expect.
For example, if you have this in your `pyproject.toml`:

```toml
[build-system]
requires = ["setuptools>=46,<47", "wheel>=0.34,<1.0"]
```

These are considered `dev` dependencies and will be translated in `requirements.txt` to:

```
setuptools[dev]   >=46,<47
wheel[dev]        >=0.34,<1.0
```

And into a poetry section of `pyproject.toml` as:


```toml
[tool.poetry.dev-dependencies]
setuptools        = ^46
wheel             = ^0.34
```

And into Pipenv’s `Pipfile` as:

```yaml
[dev-packages]
setuptools      = ">=46,<47"
wheel           = ">=0.34,<1.0"
```

And into an Anaconda `environment.yml` as:

```yaml
  # @ ::dev
  - setuptools   >=46,<47
  - wheel        >=0.34,<1.0
```

And into an Anaconda recipe `meta.yaml` as:

```
requirements:
  build:
    - setuptools   >=46,<47
    - wheel        >=0.34,<1.0
```

Note that `setuptools` is probably *not* a dependency to build with conda.
You can configure that behavior in `.tyrannosaurus`.
Also note that Anaconda recipes can be generated from PyPi packages using `conda-build`,
but the `build` section won’t be translated (from what I’ve seen).


#### Pipenv and poetry lock files:

Lock files for pipenv (`Pipfile.lock`) and poetry (`poetry.lock`) are not affected.
This is by design! Use those tools to manage them.


### Getting help:
You can always run `tyrannosaurus help` for usage help.
For reference, here are the commands:
- `tyrannosaurus new` (create a new project skeleton)
- `tyrannosaurus reqs` (sync dependencies and project info)
- `tyrannosaurus find` (find imports and sync them plus project info)
- `tyrannosaurus check` (only emit information)
- `tyrannosaurus sync-info` (only sync project info)
- `tyrannosaurus build-cache` (just build or update the cache)
- `tyrannosaurus clear-cache` (just delete the cache)
- `tyrannosaurus help`


### Things to do

This section may be helpful if you’re new to the Python build infrastructure.
Some config files are for tools that need some extra setup.
First, make sure to push to a Git repository.
I also recommend installing and using [poetry](https://github.com/python-poetry/poetry).
Make sure to commit your `poetry.lock` file.
Register on PyPi, the PyPi test repository, and readthedocs and set up builds on either Travis or CircleCI, and perhaps register on [coveralls](https://coveralls.io).
These last three tools are commercial but are currently free for open source projects and/or academic use.

Other tools of interest are set up to run in [Tox](https://github.com/tox-dev/tox)
in the default project skeleton (listed in `pyproject.toml`).
These include [black](https://github.com/psf/black), [isort](https://github.com/timothycrosley/isort),
[mypy](http://mypy-lang.org/), and [coveragepy](https://github.com/nedbat/coveragepy).

Consider using [PyPi’s test repository](https://test.pypi.org) before uploading to the main one.
Note that you still can’t delete it or update it with the same version number.
Finally, you may want to upload to conda-forge or generate a Docker image.
Here’s the command for PyPi test upload:

```
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```




### Configuring

Occasionally you may need to modify tyrannosaurus’s behavior.
For example, you may want it to leave your `requirements.txt` untouched or modify a file called `all-requirements.txt`.
Or, maybe you want to change the way it chooses version ranges.
To do this, add a `.tyrannosaurus` file in your root.
More information is in the docs.


### Compatibility and problems

Tyrannosaurus is your average mesozoic-era dinosaur, compatible with Python 3.6+.
However, you can modify any project it generates to expand the compatibility as you see fit.
UTF-8 is assumed in all files, and other encodings may cause issues.

It’s not very intelligent, so it will back up your files first.
For example, it will make a `.tyrannosaurus-cache/requirements.txt-2020-04-05T152203.1151492`.
You can tell it to clean up older versions with `tyrannosaurus clean`.

### Building, extending, and contributing

[New issues](https://github.com/dmyersturnbull/tyrannosaurus/issues) and pull requests are welcome.

Tyrannosaurus is bootstrapped—built using itself.
If you fork it, you can modify its files and install your fork to modify its default project structure.
To modify the default `README.md`, modifying this one won’t work.
The same is true for some other files that are also used to describe tyrannosaurus itself.
Files under `docs/` and `tyrannosaurus/` are not included in new projects.
To work around this, you can add or modify files under `tyrannosaurus/resources/auto/`.
These files will be copied to new projects.
In text files, `${{project}}` will be replaced with the project name.


Conda build:
1. `pip install m2-patch`
2. `conda skeleton pypi tyrannosaurus`


### meta info

Tyrannosaurus was developed by Douglas Myers-Turnbull and is licensed under the [Apache License, version 2.0](https://www.apache.org/licenses/LICENSE-2.0).
He wrote it after making 18 Git commits trying to configure readthedocs and PyPi.
This avoids that struggle for 99% of projects.

Pipenv and poetry evolved independently after conda.
For relevant discussion, see:
- [this issue on poetry](https://github.com/python-poetry/poetry/issues/190)
-  [this umbrella issue](https://github.com/kiwi0fruit/misc/issues/4).

Related projects, some of which tyrannosaurus uses:
- [anaconda](https://anaconda.org/)
- [conda-forge](https://conda-forge.org/)
- [conda-pack](https://conda.github.io/conda-pack/)
- [cpip](https://github.com/eigentechnologies/cpip), a wrapper around conda-pack
- [pipenv](https://github.com/pypa/pipenv)
- [poetry](https://github.com/python-poetry/poetry), which is excellent
- [pipreqs](https://github.com/bndr/pipreqs), which finds imports
- [pur](https://github.com/alanhamlett/pip-update-requirements), which searches pypi
- [pipdeptree](https://github.com/naiquevin/pipdeptree), which builds a dependency tree
- [pip-conflict-checker](https://github.com/ambitioninc/pip-conflict-checker), which is unmaintained
- [pip-check](https://github.com/bartTC/pip-check/), which formats `pip list` output
- [pip-chill](https://github.com/rbanffy/pip-chill), which lists top-level dependencies
- the [pip check](https://pip.pypa.io/en/stable/reference/pip_check) command, which doesn’t do what you might hope
- [python-semantic-release](https://github.com/relekang/python-semantic-release), which is not used

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
