Tyrannosaurus
====================================

.. toctree::
    :maxdepth: 1

    usage
    guide
    synchronization

Tyrannosaurus is an opinionated 2020 Python template
that comes with a tool to synchronize duplicate metadata across your build.

Use it to generate ready-to-go Python projects
with easy testing and Github actions for testing and publishing.
Lints on commit, tests on commit, and deploys to PyPi when you make a release on Github.

You can either use the command-line interface,
or just clone from the `Github source <https://github.com/dmyersturnbull/tyrannosaurus>`_.
The command-line variant will generate slightly better code
by filling in your project name and options.
To install, run: ``pip install tyrannosaurus``


.. warning::

    Tyrannosaurus is in an alpha build.
    Generally works pretty well, but the ``sync`` command does less than advertised.


What’s wrong with pip or anaconda?
----------------------------------

Quite a lot, actually. A ``setup.py``` can contain arbitrary code, which
is a security risk, and metadata can’t be extracted without installing.
Pip also doesn’t check for dependency conflicts.
Anaconda does resolve dependencies, but some packages are not on Anaconda,
and some are not kept up-to-date. It can also make for a more complex build process.


List of integrations
--------------------

New projects are configured for:

- Build: `Poetry <https://github.com/python-poetry/poetry>`_, Tox, Conda,
  `DepHell <https://github.com/dephell/dephell>`_, wheels, sdist
- Test: Tox, pytest, Coverage, Bandit
- Style: Black, Flake8, MyPy, pycodestyle, pydocstyle
- Hooks: `EditorConfig <https://editorconfig.org>`_, pre-commit-hooks
- Documentation: ReadTheDocs, Sphinx, sphinx-autoapi
- CI: Travis, Github actions
- Publish: Twine, Docker, Conda-Forge (with `grayskull <https://github.com/marcelotrevisani/grayskull>`_)
