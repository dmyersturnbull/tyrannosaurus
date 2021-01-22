Tyrannosaurus overview
======================

.. toctree::
    :maxdepth: 1

    index
    new
    build
    guide
    synchronization
    anaconda
    databases
    ref

`Tyrannosaurus <https://github.com/dmyersturnbull/tyrannosaurus>`_ is an opinionated Python
template for 2021 that comes with a tool to synchronize duplicate metadata across your build.

Use it to generate ready-to-go Python projects
with easy testing and Github actions for testing and publishing.
Lints on commit, tests on commit, and deploys to PyPi when you make a release on Github.
Also see the `Tyrannosaurus readme <https://github.com/dmyersturnbull/tyrannosaurus/blob/master/README.md>`_.

You can either use the command-line interface,
or just clone from the `Github source <https://github.com/dmyersturnbull/tyrannosaurus>`_.
The command-line variant will generate slightly better code
by filling in your project name and options.
To install, run: ``pip install tyrannosaurus``


.. warning::

    Tyrannosaurus is in an alpha build.
    Generally works quite well, but the ``sync`` command does less than advertised.


What’s wrong with pip or anaconda?
----------------------------------

Quite a lot, actually. A ``setup.py`` can contain arbitrary code, which
is a security risk, and metadata can’t be extracted without installing.
Pip also doesn’t check for dependency conflicts.
Anaconda does resolve dependencies, but some packages are not on Anaconda,
and some are not kept up-to-date. It can also make for a more complex build process.


List of integrations
--------------------

A similar list is in the `readme <https://github.com/dmyersturnbull/tyrannosaurus>`_.
Briefly, projects are configured for:

- Python 3.8, 3.9, and 3.10
- Build: `Poetry <https://github.com/python-poetry/poetry>`_, Tox, Conda, wheels, sdist
- Test: Tox, pytest, Coverage, Bandit, BugBear, Dependabot
- Style: Black, Flake8, MyPy, pycodestyle, pydocstyle
- Hooks: `EditorConfig <https://editorconfig.org>`_, pre-commit-hooks
- Documentation: ReadTheDocs, Sphinx, sphinx-autoapi
- CI: Travis, Github actions, Azure pipelines
- Coveralls, CodeCov, CodeClimate, and CodeQL
- Publish: Twine, DockerHub, Conda-Forge (with `grayskull <https://github.com/marcelotrevisani/grayskull>`_)
- Reference: `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
  `Github issue templates <https://help.github.com/en/github/building-a-strong-community/setting-guidelines-for-repository-contributors>`_,
  `Citation File Format <https://github.com/citation-file-format/citation-file-format>`_,
  `codemeta.json <https://codemeta.github.io/>`_
