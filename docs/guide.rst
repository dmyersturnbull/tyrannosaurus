To-do reference for new projects
================================

This doc is linked by Tyrannosaurus after running ``tyrannosaurus new``.
It may be especially helpful for users new to Python packaging.
See the `new project guide <https://tyrannosaurus.readthedocs.io/en/stable/new.html>`_
for usage of ``new`` and more detailed information about some of these steps.

To-do list
----------

These are suggested steps for after running ``tyrannosaurus new --track``.
The ``--track`` option to the ``new`` command tracks ``usernameororg/project``.
Alternatively, copy the files Tyrannosaurus generated into your repo,
or use ``--track`` and just modify the git remote afterward.

.. tip::

    Check ``git config user.name``, ``git config user.name``, and your
    GPG keys: ``git config --global user.signingkey``


Getting your first commit on GitHub
+++++++++++++++++++++++++++++++++++

1. **Create a repo:** Create an *non-initialized* repository under ``userororgname/projectname``.
   (Don’t add a readme, etc.) **Install `Probot Settings <https://github.com/probot/settings>`_:**  in your repo.
3. **Delete unwanted files:** Delete ``.github/labels.json``, ``.github/workflows/labels.yml``, ``.travis.yml``,
   and ``.azure-pipelines.yml``, assuming you’re not using them. You might also not want ``codemeta.json``,
   ``CITATION.cff``, ``environment.yml``, or ``Vagrantfile``.
4. Modify ``pyproject.toml`` and ``README.md``.
5. Add an entry to ``CHANGELOG.md`` and run ``git commit -m "feat: initial code"`` (probably twice).

.. tip::

    If a linter such as black fails on commit, just run git commit again to accept the linted version.

.. tip::

    Always run ``tyrannosaurus sync`` or ``poetry lock`` after modifying dependencies.

.. tip::

    A `Commitizen <https://github.com/commitizen-tools/commitizen>`_ pre-commit hook checks commit
    messages. If it’s too restrictive, modify ``[tool.commitizen]`` in pyproject.toml
    or remove the pre-commit-config entry.


Configuring external integrations
+++++++++++++++++++++++++++++++++

External services require additional steps.
These are making accounts, installing GitHub apps, adding webhooks, and adding GitHub secrets.
See
the `report config guide <https://tyrannosaurus.readthedocs.io/en/stable/new.html#manual-steps-to-configure-reports>`_
for discussion.

1. **PyPi:** On `PyPi <https://pypi.org>`_, create a new project and get a repo-specific token.
   In your GitHub secrets page (under *Settings*), add ``PYPI_TOKEN``.
2. **Docker Hub:** Tell `DockerHub <https://hub.docker.com/>`_ to track your repo with source ``/v[0-9]+.*/`` and
   tag ``{sourceref}``. On your GitHub repo ⮞ Settings ⮞ Webhooks ⮞ your docker hook ⮞ Edit, check ``Releases``.
5. **Readthedocs:** Set up readthedocs to track your repo.
6. **Code quality / coverage (1):** Set up Code Climate, Scrutinizer, and either CodeCov or Coveralls.
7. **Code quality / coverage (2):** Add either ``COVERALLS_REPO_TOKEN`` or ``CODECOV_TOKEN`` to your GitHub secrets.
8. **Slack notifications:** For important success/failure notifications,
   add ``SLACK_WEBHOOK`` as a GitHub secret and set ``use_slack=false`` in ``.github/action-options.json``.

.. tip::

    If you choose not to install Probot Settings, check out the suggested branch protection rules in
    ``.github/settings.yml``.
    Also confirm that Dependabot *alerts* and *security updates* are enabled under *Security & analysis*.
    Currently, Dependabot updates are only available on a GitHub organization.


Your first GitHub release
+++++++++++++++++++++++++

Follow these steps to publish to GitHub releases, GitHub Packages, Docker Hub, and PyPi.
If you’re using the default Azure-pipelines file, you’ll also publish to Azure’s container registry.
If you want to publish to Conda-Forge, follow
the `anaconda recipe-generation steps <https://tyrannosaurus.readthedocs.io/en/stable/anaconda.html#anaconda-recipes>`_
after the package is on PyPi to get an initial recipe (``meta.yaml``) file.
Your project’s ``CONTRIBUTING.md`` will list the steps to make subsequent releases.
(See `Tyrannosaurus’s own contributing guide <https://github.com/dmyersturnbull/tyrannosaurus/blob/main/CONTRIBUTING.md>`_.)


Final thoughts
++++++++++++++

Note the normal way to update the *main* branch:
1. Push to a remote branch or fork and make a pull request against *main* branch.
2. When the pull request tests pass, submit a review on the pull request, and rebase it into *main*.


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

Commitizen can be used to generate a changelog. In my experience, those changelogs are not great because
(1) commit messages are too messy, (2) the ``feat:``, ``fix:``, etc. commit types don’t match up with
those in keep-a-changelog, (3) it fails completely if one commit message is off, (4) it’s hard to modify the style
at a later date without completely rewriting the git history or adding a plugin for Commitizen, and (5)
Commitizen destroys any extra text you add to your Changelog, such as a ”Conventions” section.
Instead, I just add to the changelog manually.

.. warning::

    Probot Settings has a `privilege escalation issue <https://github.com/probot/settings#security-implications>`_.
    Either accept that as a caveat, list ``.github/settings.yml`` in ``.github/CODEOWNERS``, or disable it after your initial push.

.. caution::

    Both ``tyrannosaurus sync`` and Commitizen’s ``bump`` copy version numbers. They won’t always play well together.
    I recommend not using it. In the future, you may be able to point ``tool.tyrannosaurus.sources.version``
    to ``tool.commitizen.version`` (leaving ``tool.commitizen.version_files`` empty).


Reference of commands
---------------------

These commands might be useful:

- ``tyrannosaurus sync`` to sync metadata and nothing else
- ``tyrannosaurus clean --aggressive`` to remove lots of temp files
- ``tox`` to build, test, build docs, and run some static analyses
- ``poetry update`` to find updated dependency versions (major or minor)
- ``tyrannosaurus recipe`` to generate a Conda recipe

These commands are run automatically via either Tox or a GitHub action,
but you can run them locally too:

- ``poetry install`` to install and nothing more
- ``poetry build`` to build wheels and sdists
- ``poetry publish`` to upload to PyPi
- ``docker build .`` to build a docker image
