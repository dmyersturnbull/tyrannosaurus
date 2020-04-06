# Tyrannosaurus

[![Build status](https://img.shields.io/pypi/status/tyrannosaurus)](https://pypi.org/project/tyrannosaurus/)
[![Latest version on
PyPi](https://badge.fury.io/py/tyrannosaurus.svg)](https://pypi.org/project/tyrannosaurus/)
[![Supported Python
versions](https://img.shields.io/pypi/pyversions/tyrannosaurus.svg)](https://pypi.org/project/tyrannosaurus/)
[![Documentation
status](https://readthedocs.org/projects/tyrannosaurus/badge/?version=latest&style=flat-square)](https://readthedocs.org/projects/tyrannosaurus/)
[![Travis](https://travis-ci.org/kokellab/tyrannosaurus.svg?branch=master)](https://travis-ci.org/kokellab/tyrannosaurus)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

1. Generate Python projects set up with modern tools, including [Tox](https://github.com/tox-dev/tox), PyPi, and Anaconda.
2. Update dependencies listed in any format, and find conflicts.

I wrote this after making 18 Git commits trying to configure readthedocs and PyPi.
This avoids that struggle for 99% of projects.

Install with `pip install tyrannosaurus`.
Create a project with `tyrannosaurus init` for a structure like this one, modify it as you see fit, and use `tyrannosaurus reqs`, `tyrannosaurus bump`,  and/or `tyrannosaurus find` to manage dependencies.
These commands will keep any requirements.txt, setup.py, Pipfile, Poetry dependencies, conda recipes, and Anaconda environment files in sync. And they'll tell you about conflicting, cyclic, and duplicate dependencies.

**Non-goal:**
This little project does not introduce a new abstraction for dependency management.
It only makes it easier to start new projects and sync or migrate between formats.
[Anaconda](https://anaconda.org/), [conda-forge](https://conda-forge.org/), [pipenv](https://github.com/pypa/pipenv), and [poetry](https://github.com/python-poetry/poetry) are great places to look.

⚠ Not finished yet! The scripts are scattered everywhere. This should be ready in late April.

### creating a new project

```
tyrannosaurus init mynewproject
```

Your new project is ready for PyPi, Sphinx, Sphinx API docs, readthedocs, Git, Tox, Travis, CircleCI, and conda-forge.
The Tox config will generate PyPi-ready source and wheel builds, and even a conda package for you!
Your project's version is specified only once, in `yourpackage/__init__.py`.

You can modify your project freely after, and tyrannosaurus will still understand it.
Of course, `init` also has some command-line options. Run `tyrannosaurus init --help` to see them.
You can choose another license with `tyrannosaurus init mynewproject --license "MIT"`.

### managing dependencies

Tyrannosaurus's best feature is managing and translating dependencies.
It keeps your dependencies consistent between requirements.txt, conda recipes, Anaconda environment files, Pipfiles (pipenv), and setup.py files.
If there is a merge conflict, it will keep the highest version.
Just run:

```
tyrannosaurus reqs
```
No pun intended, of course.

You can also update the versions to the most recent available on PyPi and your Anaconda channels:
It will report inconsistencies between Anaconda channel versions and versions on PyPi.

```
tyrannosaurus bump
```

Finally, you can use [pipreqs](https://github.com/bndr/pipreqs) to find dependencies from your imports:

```
tyrannosaurus find
```


All of these commands will tell you about dependency conflicts.
Note that [pip does not know about dependency trees](https://github.com/pypa/pip/issues/988),
which can be a serious problem. If you only want this, call `tyrannosaurus check`.


### optional dependencies

By the way, you can distinguish between requirements and optional dependencies in all of these types.
For example, your requirements.txt might look like this:
```
click                  >=7.1,<8.0
hypothesis[test]       >=5.8,<6.0
pytest[test]           >=5.4,<6.0
```

In `setup.py`, these are listed in `extras_require`.
Unfortunately, `environment.yml` files don't support optional dependencies.
We get around this using comments starting with `# @`. See the docs for more info.

### configuring

Occasionally you may need to modify tyrannosaurus's behavior.
For example, you may want it to leave your `requirements.txt` untouched or modify a file called `all-requirements.txt`.
Or, maybe you want to change the way it chooses version ranges.
To do this, add a `.tyrannosaurus` file in your root.
More information is in the docs.


### compatibility and problems

Tyrannosaurus is your average mesozoic-era dinosaur, compatible with Python 3.4+. 
However, you can modify any project it generates as you see fit.

It's not very intelligent, so it will back up your files first.
For example, it will make a `.requirements.txt.bak-2020-04-05T152203.1151492`.
You can tell it to clean up older versions with the global `--clean` flag.

Please note that lock files for pipenv and poetry are not affected by design.

### building, extending, and contributing

[New issues](https://github.com/kokellab/tyrannosaurus/issues) and pull requests are welcome.

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

Related projects, some of which tyrannosaurus uses:
- [anaconda](https://anaconda.org/)
- [conda-forge](https://conda-forge.org/)
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
