Tyrannosaurus
====================================

.. toctree::
    :maxdepth: 1

Tyrannosaurus is an opinionated 2020 Python template.
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
    Generally works pretty well, but the `sync` command does less than advertised.


Create a new project
--------------------

You can use Tyrannosaurus to create a new project.
Run: ``tyrannosaurus new myproject``.
It will clone the most recent version and fill in information.
It will guess the authors and Github username from your git config.
But you can pass those in with ``--authors`` (comma-separated) and ``--user`` (single item).
You can also choose a different license using ``--license``.
Choices are Apache 2, CC0, CC-BY, CC-BY-NC, GPL 3, LGPL, and MIT.
See ``tyrannosaurus new --help`` for more info.

After, modify your project as needed,
especially by setting your metadata and dependencies in ``pyproject.toml``.
You may consider adding ``tyrannosaurus clean``, ``tyrannosaurus sync``,
and/or ``tyrannosaurus env`` to your tox config.
Finally, you may want to modify the ``.github/labels.json`` file.
When you commit, your Github labels will be replaced with these.

.. caution::

    Will replace your Github labels each time you commit.
    Either edit the ``.github/labels.json`` file or disable by deleting
    ``.github/workflows/labels.yml``.


To get the Github publish action working, you need to:

1. Make an account on pypi.org if you don’t have one.
2. Make a new single-repo token on PyPi.
3. In your Github secrets page, add ``PYPI_TOKEN``.


Build and test
--------------------

This section assumes you will be using `Poetry <https://python-poetry.org/>`_
and `Tox <https://tox.readthedocs.io/>`_.
If you don’t have Poetry, you should `install it <https://python-poetry.org/docs/#installation>`_.
To will be installed as a dependency when you run ``poetry install``.

After that, you can always run ``tox`` to build and run tests.
The ``tox.ini`` runs a sequence of commands to build, synchronize, clean,
and test your project; create a new ``poetry.lock``; and generate HTML docs.
Take a look at the ``testenv`` section to see the commands.
The Github workflows ``build.yml`` and ``publish.yml`` install Poetry and run Tox,
so whatever you add to ``tox.ini`` will be done in Github.

.. tip::
    You can bump major or minor versions of your dependencies using ``poetry update``.


Tyrannosaurus sync
--------------------

Running Tox calls ``tyrannosaurus sync``.
This command copies some project metadata from pyproject.toml to other files and between sections.
These are the required Python versions, development requirements, and line length.
It will also warn you if other information seems inconsistent, such as
a license file not matching.

You can configure this behavior in pyproject.toml
under ``[tool.tyrannosaurus.sources]`` and ``[tool.tyrannosaurus.targets]``.
``targets`` specifies what files and directories to update.
Filename extensions and some directory names are omitted.
The information to update will be decided from the filenames.
For example, ``init`` will include the copyright statement from ``tool.tyrannosaurus.sources.copyright``.
The sources can be either literal values surrounded in single quotes,
or the names of other settings in pyproject.toml.
You can use ``${today}`` to refer to the current date and ``${datetime}`` for the datetime.
``datetime`` will be in the format ``2020-05-07 20:21``.
You can access individual fields as expected, such as ``${datetime.hour}}`` for ``'20'``.

.. note::

    Tyrannosaurus always generates backups before modifying.
    These are saved in ``.tyrannosaurus`` but are cleared on the next Tox build.



To-do list
--------------------

For reference, here are some steps to consider after creating a new repository:

- Configure Git to use your GPG keys: ``git config --global user.signingkey``
- Set up automated code review (ex `codeclimate <https://codeclimate.com/>`_)
- Review `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_,
  `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_),
   and `Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`_)


Anaconda environment file
-------------------------

You can generate an environment yml file using: ``tyrannosaurus env``.
It will check for packages on Conda-Forge and move packages not found to the ``pip:`` section.


Anaconda recipes
--------------------

This describes how to generate a Conda recipe and
[upload it to `Conda-Forge <https://conda-forge.org/#add_recipe>`_.
Your desired version must already be published on PyPi.

1. Run ``tyrannosaurus recipe``, which will run grayskull.
2. Check over your new recipe in ``recipes/projectname/meta.yaml``.
3. Fork from  `staged-recipes <https://github.com/conda-forge/staged-recipes>`_.
4. Copy your recipe from ``recipes/projectname/meta.yaml`` into the repo (keeping the path).
5. Make a pull request. If everything goes well, it will be on Conda-Forge soon!

.. tip::

    On Windows, you may need to run ``conda install m2-patch`` first.


What’s wrong with pip or anaconda?
--------------------

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


List of sync targets
--------------------

Here are most of the available synchronization targets:

- Copyright, status, and date in ``__init__.py``
- Dev dependencies between ``tool.poetry.dev-dependencies``, ``tool.poetry.extras``, and ``tox.ini``
- An ``all`` optional dependency list with all optional non-dev packages
- Dependencies for building docs in ``docs/conf.py`` and ``docs/requirements.txt``
- Code line length between ``isort``, ``black``, and ``pycodestyle``
- Python version in ``pyproject.toml``, ``tox.ini``, ``.travis.yml``, ``black``, and ``readthedocs.yml``
- Copyright in ``docs/conf.py``
- Poetry version in ``Dockerfile``
- Authors and year listed in the license file
- Dev versions in ``.pre-commit-config.yaml``
- ``--maintainers`` arg for Grayskull in ``tox.ini``
- ``doc_url``, ``dev_url``, and ``license_file`` in ``meta.yaml``
- Most recent version in ``CHANGELOG.md`` assuming `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_


Reference of commands
---------------------

These commands might be useful:

- ``pre-commit install`` to configure pre-commit hooks
- ``tox`` to sync metadata, build, install, build docs, and test
- ``poetry bump`` to bump dependency versions (major or minor)
- ``tyrannosaurus recipe`` to generate a Conda recipe (see below)

And these commands are run automatically via either Tox or a Github action:

- ``tyrannosaurus sync`` to sync metadata and nothing else
- ``tyrannosaurus clean --aggressive`` to remove lots of temp files
- ``poetry install`` to install and nothing more
- ``poetry build`` to build wheels and sdists
- ``poetry publish`` to upload to PyPi
- ``docker build .`` to build a docker image
