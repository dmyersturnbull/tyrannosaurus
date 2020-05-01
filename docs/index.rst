Tyrannosaurus
====================================

.. toctree::
    :maxdepth: 1

To install, run:

.. code-block:: text

    pip install tyrannosaurus

..warning::

    Tyrannosaurus is very new and will undergo changes.


Create a new project
--------------------

First, run:

.. code-block:: text

    tyrannosaurus new myproject

Then modify your project as needed.
Almost all of the configurable entities are in ``pyproject.toml``.
A copyright string is listed in ``myproject/__init__.py``.
Finally, you may want to modify ``tox.ini``.


Build and test
--------------------

.. note::

    This section assumes you will be using `Poetry <https://python-poetry.org/>`_
    and `Tox <https://tox.readthedocs.io/>`_.
    If you don’t have Poetry, you should `install it <https://python-poetry.org/docs/#installation>`_.
    If you really don’t want to use Poetry,
    modify ``tox.ini`` and remove references to Poetry and ``tyrannosaurus sync``.

The ``tox.ini`` runs a sequence of commands to build, lint, synchronize, clean,
and test your project; create a new ``poetry.lock``; and generate HTML docs.
Take a look at the ``testenv`` section to see the commands.
Basically, you can just run:

.. code-block:: text

    tox

.. tip::
    You can bump major or minor versions of your dependencies using ``poetry update``.
    To publish your project on `PyPi <https://pypi.org/>`_, run ``poetry publish``.


Tyrannosaurus sync
--------------------

Running ``tox`` calls ``tyrannosaurus sync``.
This command copies some project metadata from ``pyproject.toml`` to other files
and between sections.
These are the required Python versions, development requirements,
and line length.
It will also warn you if other information seems inconsistent, such as
a license file not matching.

You can configure this behavior in the ``tool.tyrannosaurus`` section
of ``pyproject.toml``.



Anaconda recipes
--------------------

After publishing to PyPi, you can build an Anaconda recipe using:

.. code-block:: text

    conda skeleton pypi myproject

On Windows, you may need to run ``conda install m2-patch`` first.
Your recipe file (``meta.yaml``) may still need some manual tweaking.
