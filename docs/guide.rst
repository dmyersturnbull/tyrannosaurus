To-do reference for new projects
================================

Guide for new projects. This doc linked by Tyrannosaurus after running ``tyrannosaurus new``.
It may be especially helpful for users new to Python packaging.
See the `new project guide <https://tyrannosaurus.readthedocs.io/en/stable/new.html>`_
for usage of ``new`` and more detailed information about some of these steps.

To-do list
----------

These steps are provided for reference and for new users.
Consider following them after running ``tyrannosaurus new --track``.
These are recommended steps; of course, you can modify them as you see fit.

.. tip::

    First, make sure Git is configured correctly.
    Check ``git config user.name`` and ``git config user.name``.
    Make sure it knows about your GPG keys: ``git config --global user.signingkey``

.. note::

    The ``--track`` option to the ``new`` command tracks ``usernameororg/project``.
    If you did not use ``--track``, you should create ann empty (non-initialized) Github repo and track it with
    ``git remote add origin mygithuburl`` in your new repo follow it with ``git checkout -b main``.
    Then just copy your generated project files to the repo and run ``pre-commit install``.


Repo configuration and first commit
+++++++++++++++++++++++++++++++++++

Here’s what you need to get your first commit on Github.

1. **Create a repo:** Create an *empty* repository under ``userororgname/projectname``.
   Do **not** add a readme, license, or gitignore.
2. **Use Probot:** Install `Probot Settings <https://github.com/probot/settings>`_ in your repo.
3. **Delete unwanted files:** Delete ``.github/labels.json``, ``.github/workflows/labels.yml``, ``.travis.yml``,
   and ``.azure-pipelines.yml``, assuming you’re not using them. You might also not want ``codemeta.json``,
   ``CITATION.cff``, ``environment.yml``, or ``Vagrantfile``.
4. Modify ``pyproject.toml`` and ``README.md``.
5. Add an entry to ``CHANGELOG.md`` and run ``git commit -m "feat: add initial code"`` (probably twice).


.. hint::

    When you commit, pre-commit hooks are run. If a linter such as black ran and failed,
    just run again git commit again on the now-linted version. Push to the main branch after committing.

.. tip::

    Remember to always sync metadata (``tyrannosaurus sync``) or at least ``poetry lock`` before committing or testing.
    You can create a custom pre-commit hook to do this before each commit.


Configuring external integrations
+++++++++++++++++++++++++++++++++

Next, external services require their own steps that you’ll need to follow.
This consists of (1) making accounts, (2) installing Github apps, (3) adding webhooks, and (4) adding Github secrets.

1. **PyPi (1):** On `PyPi <https://pypi.org>`_, create a new project and get a repo-specific token.
2. **PyPi (2):** In your Github secrets page (under *Settings*), add ``PYPI_TOKEN``.
3. **Docker Hub (1):** Tell `DockerHub <https://hub.docker.com/>`_ to track your repo with source ``/v[0-9]+.*/`` and
   tag ``{sourceref}``.
4. **Docker Hub (2):** On your Github repo ⮞ Settings ⮞ Webhooks ⮞ your docker hook ⮞ Edit, check ``Releases``.
5. **Readthedocs:** Set up readthedocs to track your repo.
6. **Code quality / coverage (1):** Set up Code Climate, Scrutinizer, and either CodeCov or Coveralls.
7. **Code quality / coverage (2):** Add either ``COVERALLS_REPO_TOKEN`` or ``CODECOV_TOKEN`` to your Github secrets.

.. tip::

    If you choose not to install Probot Settings but are interested in the settings, take a look at the
    ``.github/settings.yml`` file. The most important part is the branch protection rules.
    Also confirm that *Dependabot alerts* and *Dependabot security updates* are enabled under *Security & analysis*.
    Currently, this is only possible on a Github organization repo.


Configuring external integrations
+++++++++++++++++++++++++++++++++

See
the `report config guide <https://tyrannosaurus.readthedocs.io/en/stable/new.html#manual-steps-to-configure-reports>`_
for more discussion.

1. Push to a new remote branch and make a pull request to your *main* branch (on Github).
2. When the pull request tests pass and you submit a review, rebase it into *main*.


Your first real release
+++++++++++++++++++++++

Follow these steps to publish to Github releases, Github Packages, Docker Hub, and PyPi.
If you’re using the default Azure-pipelines file, you’ll also publish to Azure’s container registry.
If you want to publish to Conda-Forge, follow
the `anaconda recipe-generation steps <https://tyrannosaurus.readthedocs.io/en/stable/anaconda.html#anaconda-recipes>`_
right after. Only two steps:

1. Wait for the test and link-check actions to pass. Then, just create a new Github Release.
2. Watch the wokflows run, the packages get published, and shields get updated.

.. caution::

    The *publish* workflow does **not** run your tests because it’s assumed that the tests already passed
    from the push to *main* and/or pull request to *main*.
    This would be circumvented if you pushed directly to main and then didn’t wait for the tests to pass.
    You need to make sure that the *commit* workflow succeeds before creating a Github Release.


Things to consider reviewing
++++++++++++++++++++++++++++

Review `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_,
`Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_, and
`Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`_.
Consider `getting a DOI <https://guides.github.com/activities/citable-code/>`_ for scientific software.
If you’re using Jupyter, consider adding [nbstripout](https://github.com/kynan/nbstripout) to your
``pre-commit-config.yaml`` to avoid ending up with a massive git history.
If you want to create a package on Conda-Forge, see the
`anaconda integration guide <https://tyrannosaurus.readthedocs.io/en/stable/anaconda.html#anaconda-recipes>`_.


You may want to add new code quality integrations, like  `codacy <https://www.codacy.com/>`_.
Consider adding `shields <https://shields.io/>`_ for those.
Other good tools to consider include [github-labeler](https://github.com/marketplace/actions/github-labeler).
and [Towncrier](https://pypi.org/project/towncrier/).

.. tip::

    If you’re following Conventional Commits, consider using messages of this form:
    ``[feat|fix|BREAKING CHANGE]: [add|remove|change|fix] [rest of message]``.
    This has the advantage that each commit (from the second term, add/remove/change/fix)
    maps directly to sections in Keep a Changelog. If you’re properly squashing commits
    into *main*, you can even generate a quality changelog from the commit messages.


Reference of commands
---------------------

These commands might be useful:

- ``tyrannosaurus sync`` to sync metadata and nothing else
- ``tyrannosaurus clean --aggressive`` to remove lots of temp files
- ``tox`` to build, test, build docs, and run some static analyses
- ``poetry update`` to find updated dependency versions (major or minor)
- ``tyrannosaurus recipe`` to generate a Conda recipe

These commands are run automatically via either Tox or a Github action,
but you can run them locally too:

- ``poetry install`` to install and nothing more
- ``poetry build`` to build wheels and sdists
- ``poetry publish`` to upload to PyPi
- ``docker build .`` to build a docker image
