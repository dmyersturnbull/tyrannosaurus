To-do reference for new projects
================================

Guide for new projects.
This may be especially helpful for users new to Python packaging.


To-do list
----------

These steps are provided for reference and for new users.
Consider following them after running ``tyrannosaurus new --track``.

.. tip::

    First, make sure Git is configured correctly.
    Check ``git config user.name`` and ``git config user.name``.
    Make sure it knows about your GPG keys: ``git config --global user.signingkey``

.. note::

    If you did not use ``--track``, you should create ann empty (non-initialized) Github repo and track it with
    ``git remote add``. You will also need to run run ``pre-commit install``.


1. Remove features of the Github repo that you don’t want (such as the wiki).
2. Set up branch protection rules for *main*. I recommend *Require pull request reviews before merging* and *Require status checks to pass before merging*.
3. In your newly created project dir, remove unwanted files, such as ``.travis.yml``.
4. Modify ``pyproject.toml``, ``README.md``, and ``.github/labels.json`` as needed.
5. Update ``CHANGELOG.md`` and run ``git commit``.
6. Confirm that *Dependabot alerts* and *Dependabot security updates* are enabled under *Security & analysis* (if you’re able).
7. On `PyPi <https://pypi.org>`_, create a new project and get a repo-specific token.
8. In your Github secrets page (under *Settings*), add ``PYPI_TOKEN``.
9. Tell `DockerHub <https://hub.docker.com/>`_ to track your repo with source ``/v[0-9]+.*/`` and tag ``{sourceref}``.
10. On your Github repo ⮞ Settings ⮞ Webhooks ⮞ your docker hook ⮞ Edit, check ``Releases``.
11. Set up readthedocs to track your repo.
12. Set up CodeCov, Coveralls, Code Climate, Scrutinizer, and other services you want. Add ``COVERALLS_REPO_TOKEN`` and ``CODECOV_TOKEN`` to your Github secrets (if needed).
13. Push to a new remote branch and make a pull request to your *main* branch (on Github).
14. When the pull request tests pass, merge into *main*.
14. After that workflow succeeds, create a release on Github to publish to PyPi, Dockerhub, and Github Packages.
15. Watch to see the repo badges get updated.

Review `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_,
`Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_, and
`Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`_.
Consider `getting a DOI <https://guides.github.com/activities/citable-code/>`_.
If you’re using Jupyter, consider adding [nbstripout](https://github.com/kynan/nbstripout) to your
``pre-commit-config.yaml`` to avoid ending up with a massive git history.
If you want to create a package on Conda-Forge, see the
`anaconda integration guide <https://tyrannosaurus.readthedocs.io/en/stable/anaconda.html#anaconda-recipes>`_.

.. tip::

    When you commit, pre-commit hooks are run. If a linter such as black ran and failed,
    just run again git commit again on the now-linted version. Push to the main branch after committing.

.. tip::

    Remember to always sync metadata (``tyrannosaurus sync``) or at least ``poetry lock`` before committing or testing.
    You can create a custom pre-commit hook to do this before each commit.

You may want to add new code quality integrations, like  `codacy <https://www.codacy.com/>`_.
Consider adding `shields <https://shields.io/>`_ for those.
Other good tools to consider include [github-labeler](https://github.com/marketplace/actions/github-labeler).
and [Towncrier](https://pypi.org/project/towncrier/).



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
