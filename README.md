# Tyrannosaurus

[![Build status](https://img.shields.io/pypi/status/tyrannosaurus)](https://pypi.org/project/tyrannosaurus/)
[![Latest version on
PyPi](https://badge.fury.io/py/tyrannosaurus.svg)](https://pypi.org/project/tyrannosaurus/)
[![Supported Python
versions](https://img.shields.io/pypi/pyversions/tyrannosaurus.svg)](https://pypi.org/project/tyrannosaurus/)
[![Documentation
status](https://readthedocs.org/projects/tyrannosaurus/badge/?version=latest&style=flat-square)](https://readthedocs.org/projects/tyrannosaurus/)
[![Travis](https://travis-ci.org/dmyersturnbull/tyrannosaurus.svg?branch=master)](https://travis-ci.org/dmyersturnbull/tyrannosaurus)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

##### What it does:
- Generates Python projects configured for modern build tools and ready to upload to readthedocs, PyPi, and [Conda-Forge](https://conda-forge.org/).
- Synchronizes dependencies in setup.py, setup.cfg, requirements files, conda recipes, conda envs, pipenvs, and [poetry](https://python-poetry.org/) configs.
- Lets your package's users build with the tools they prefer.

##### What it doesn't do:
- Resolve dependencies. See Poetry or Anaconda for this!
- Introduce a new path to list dependencies.

##### How to use it:

1. Install with `pip install tyrannosaurus`.
2. Create a project with `tyrannosaurus new`. Modify as you see fit.
4. Use `tyrannosaurus reqs` to synchronize your dependencies and project info (version number, description).
5. Optionally, run `tyrannosaurus reqs --latest`. This interfaces with Poetry and Conda-Forge to find package updates.

##### Conflict identification:

Poetry and Conda (and pipenv) are full dependency managers capable of identifying and resolving conflicts.
Tyrannosaurus is just smart enough to tell you when versions from Conda and PyPi cannot match.

##### ⚠ Status:

Not finished yet! The scripts are scattered everywhere. This should be ready in late April.

### creating a new project

```
tyrannosaurus new mynewproject
```

Your new project is ready for PyPi, Sphinx, Sphinx API docs, readthedocs, Git, Tox, Travis, CircleCI, and conda-forge.
The Tox config will generate PyPi-ready source and wheel builds, and even a conda package for you!
Your project's version is specified only once, in `yourpackage/__init__.py`.

You can modify your project freely after, and tyrannosaurus will still understand it.
Of course, `new` also has some command-line options. Run `tyrannosaurus new --help` to see them.
You can choose another license with `tyrannosaurus init mynewproject --license "MIT"`.

### Managing dependencies

Tyrannosaurus's best feature is managing and translating dependencies.

##### Synchronizing dependencies:

It keeps your dependencies consistent between requirements.txt, conda recipes, Anaconda environment files, Pipfiles (pipenv), and setup.py files.
If there is a merge conflict, it will keep the highest version.
Just run:

```
tyrannosaurus reqs
```
No pun intended, of course.

##### Finding new versions on repositories

You can also update the versions to the most recent available on PyPi and your Anaconda channels:
It will report inconsistencies between Anaconda channel versions and versions on PyPi.

```
tyrannosaurus reqs --latest
```

##### Preferred version ranges:

By default, tyrannosaurus will use choose version ranges corresponding to the latest major version
The rationale is that compatibility with any minor version is guaranteed but compatibility with a new major version is not.
For example, if `5.8.2` is the latest, it will choose `>=5.8,<6.0`.
A good package manager will choose `5.8.2` over `5.8` if it can, but would of course reject `4.0` and `6.0` 
This behavior can be configured (see below).

##### Finding dependencies with pipreqs:

You can also use [pipreqs](https://github.com/bndr/pipreqs) to find dependencies from your imports.
This will find packages for your imports, assume the latest versions, verify, and add them to your lists.

```
tyrannosaurus reqs --find
```

##### Handling dependency conflicts:

All of these commands will tell you about dependency conflicts through Anaconda and/or Poetry, unless neither are installed.
If you only want to find conflicts and mismatches between your lists, call `tyrannosaurus check`.
This will also use `setup.py check` to verify that the `setup.py` is valid.
And of course, it will complain if it detects errors with other files.


##### Getting help:
You can always run `tyrannosaurus help` for usage help.
For reference, here are the commands:
- `tyrannosaurus new`
- `tyrannosaurus reqs`
- `tyrannosaurus find`
- `tyrannosaurus check`
- `tyrannosaurus help`

##### Listing optional dependencies:

You can distinguish between requirements and optional dependencies.
For example, your requirements.txt might look like this:
```
click                  >=7.1,<8.0
hypothesis[test]       >=5.8,<6.0
pytest[test]           >=5.4,<6.0
```

In `setup.py`, these are listed in `extras_require`.
Unfortunately, `environment.yml` files don't support optional dependencies.
We get around this using comments starting with `# @`. See the docs for more info.

### Configuring

Occasionally you may need to modify tyrannosaurus's behavior.
For example, you may want it to leave your `requirements.txt` untouched or modify a file called `all-requirements.txt`.
Or, maybe you want to change the way it chooses version ranges.
To do this, add a `.tyrannosaurus` file in your root.
More information is in the docs.


### Compatibility and problems

Tyrannosaurus is your average mesozoic-era dinosaur, compatible with Python 3.4+. 
However, you can modify any project it generates as you see fit.

It's not very intelligent, so it will back up your files first.
For example, it will make a `.requirements.txt.bak-2020-04-05T152203.1151492`.
You can tell it to clean up older versions with `tyrannosaurus clean`.

Please note that lock files for pipenv and poetry are not affected by design.
Use these tools to manage them.

### Building, extending, and contributing

[New issues](https://github.com/dmyersturnbull/tyrannosaurus/issues) and pull requests are welcome.

Tyrannosaurus is bootstrapped—built using itself.
If you fork it, you can modify its files and install your fork to modify its default project structure.

To modify the default `README.md`, modifying this one won't work.
The same is true for some other files that are also used to describe tyrannosaurus itself.
Files under `docs/` and `tyrannosaurus/` are not included in new projects.
To work around this, you can add or modify files under `tyrannosaurus/resources/auto/`.
These files will be copied to new projects.
In text files, `${{project}}` will be replaced with the project name.


### meta info

Tyrannosaurus was developed by Douglas Myers-Turnbull and is licensed under the [Apache License, version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

I wrote it after making 18 Git commits trying to configure readthedocs and PyPi.
This avoids that struggle for 99% of projects.

Pipenv and poetry evolved independently and after conda.
For some relevant discussion, see [this issue on poetry](https://github.com/python-poetry/poetry/issues/190).
Also see [this umbrella issue](https://github.com/kiwi0fruit/misc/issues/4).

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
- the [pip check](https://pip.pypa.io/en/stable/reference/pip_check) command, which doesn't do what you might hope
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
