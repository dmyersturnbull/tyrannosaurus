Tyrannosaurus overview
======================

.. toctree::
    :maxdepth: 1

    new
    build
    guide
    synchronization
    anaconda
    databases
    ref
    dev

`Tyrannosaurus <https://github.com/dmyersturnbull/tyrannosaurus>`_ is an opinionated Python
template for 2021 that comes with a tool to synchronize duplicate metadata across your build.

Use it to generate ready-to-go Python projects
with easy testing and GitHub actions for testing and publishing.
Lints on commit, tests on commit, and deploys to PyPi when you make a release on GitHub.
Also see the `Tyrannosaurus readme <https://github.com/dmyersturnbull/tyrannosaurus/blob/master/README.md>`_.

You can either use the command-line interface,
or just clone from the `GitHub source <https://github.com/dmyersturnbull/tyrannosaurus>`_.
The command-line variant will generate slightly better code
by filling in your project name and options.
To install, run: ``pip install tyrannosaurus``


.. warning::

    Tyrannosaurus is in an alpha build.
    Generally works quite well, but the ``sync`` command does less than advertised.


What’s wrong with pip or anaconda?
----------------------------------

A lot, actually. A ``setup.py`` can contain arbitrary code, which
is a security risk, and metadata can’t be extracted without installing.
Pip also doesn’t check for dependency conflicts.
Anaconda does resolve dependencies, but some packages are not on Anaconda,
and some are not kept up-to-date. It can also make for a more complex build process.


List of integrations
--------------------

For the full list of integrations, refer to
the `readme integration list <https://github.com/dmyersturnbull/tyrannosaurus#-full-features--integrations>`_.
