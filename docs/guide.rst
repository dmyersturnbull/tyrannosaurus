To-do for new projects
======================

Guide for new projects.
This may be especially helpful for users new to Python packaging.


To-do list for new projects
---------------------------

These steps are provided for reference and for new users.
Consider following them after running ``tyrannosaurus new``.

.. tip::

    First, make sure Git is configured correctly.
    Check ``git config user.name`` and ``git config user.name``.
    Make sure it knows about your GPG keys: ``git config --global user.signingkey``

1. Remove unwanted files, such as ``.travis.yml`` if unused.
2. Modify ``.github/labels.json``, ``pyproject.toml``, and ``README.md`` as needed.
3. (Note: if you used ``--track`` with ``tyrannosaurus new``, you can skip this step.)
   Create an empty (non-initialized) Github repo and copy the files.
   Run ``pre-commit install`` and ``poetry install && tyrannosaurus sync && tox``.
5. Update ``CHANGELOG.md`` and run ``git commit``.
   If changes were needed due to failed pre-commit lint changes (such as from black),
   just run again git commit again to accept the linted version. Push to the main branch after committing.
6. On `PyPi <https://pypi.org>`_, create a new repo and get a repo-specific token.
7. In your Github secrets page (under Settings), add ``PYPI_TOKEN``.
8. Tell `DockerHub <https://hub.docker.com/>`_ to track your repo with source ``/v[0-9]+.*/`` and tag ``{sourceref}``.
9. On your Github repo ⮞ Settings ⮞ Webhooks ⮞ your docker hook ⮞ Edit, check ``Releases``.
10. Create a release on Github to publish to PyPi and Dockerhub.
11. Review `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_,
    `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_, and
    `Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`_.
12. Consider `getting a DOI <https://guides.github.com/activities/citable-code/>`_.
13. Remove features of the Github repo that you don’t want (such as the wiki).
14. If you’re using Jupyter, consider adding [nbstripout](https://github.com/kynan/nbstripout)
    to your ``pre-commit-config.yaml`` to avoid ending up with a massive git history.

.. note::

    Github made *main* the `default branch name <https://github.com/github/renaming>`_ for new repositories in
    October 2020. The provided workflows should work with either *main* or *master*.
    You’ll want ``git push origin main``, not ``git push origin master``, unless you renamed the branch.

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
