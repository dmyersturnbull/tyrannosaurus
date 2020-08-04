Building and testing your project
=================================


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

