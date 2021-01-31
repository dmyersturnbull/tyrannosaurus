Making a new template
====================================

You can generate a new template. After forking Tyrannosaurus,
modify the files under ``tyrannosaurus/resources/``.
Files are renamed according to some simple rules, described below.
Note that Tyrannosaurus’s own source files are deleted.

.. note::

    The generated files are mostly trivial and are not marked as inheriting Tyrannosaurus’s Apache 2.0 license. The ``tests/__init__.py`` file contains nontrivial code and should retain its copyright notice in the module docstring if it’s kept.

``tyrannosaurus new`` follows approximately these steps:
1. It clones the repo and checks out the correct tag (according to ``--tyranno``).
2. It copies the correct license file from ``tyrannosaurus/resources/`` and deletes the others.
3. It copies all other files from ``tyrannosaurus/resources``, with modified paths.
   Files are allowed to be overwritten. For example, ``tyrannosaurus/resources/README.md`` will
   replace Tyrannosaurus’s own ``README.md``.
4. It substitutes ``$${...}`` parameters in the files it copied.

Paths under ``tyrannosuaurs/resources/`` are modified according to these rules:
- ``@`` is a path separator (e.g. ``/`` on Linux).
- ``$pkg`` and ``$project`` are replaced with their values.
  (``$pkg`` is just ``$project``, lowercase, with ``.``, ``-``, and ``-`` stripped.)
- Double-extensions ending in ``.txt`` are fixed.
  For example, ``.toml.txt`` is changed to ``.toml``.
  (Formally, we substitute ``^.*?(\.[^.@]{1,5})\.txt$`` with capture group 1.)

*In addition*, the ``.github/`` directory is copied directly, in a 1-1 file mapping.
Finally, ``tyrannosaurus/`` is deleted.

.. note::

    No files under ``.github/`` have copies under ``tyrannosaurus/resources``.
     If you want to use parameters in template files for these files,
    you can make and modify copies under, for example, ``tyranonosaurus/resources/.github@ISSUE_TEMPLATE@bug.md``.


Here the substitutions made in text files:

=========================   ==================================
 parameter                   example
=========================   ==================================
``$${today}``                ``2021-01-06``
``$${today.year}``           ``2020``
``$${today.month}``          ``01``
``$${today.Month}``          ``January``
``$${today.day}``            ``06``
``$${now}``                  ``2021-01-06 14:37:03 +03:00``
``$${now.iso}``              ``2021-01-06T14:37:03+03:00``
``$${now.utc}``              ``2021-01-06 14:37:03 Z``
``$${now.utciso}``           ``2021-01-06T14:37:03+00:00``
``$${now.hour}``             ``14``
``$${now.minute}``           ``37``
``$${now.second}``           ``03``
``$${project}``              ``my special-project``
``$${Project}``              ``My Special-Project``
``$${PROJECT}``              ``MY SPECIAL-PROJECT``
``$${pkg}``                  ``myspecialproject``
``$${Pkg}``                  ``Myspecialproject``
``$${license}``              ``gpl2``
``$${license.family}``       ``GPL``
``$${license.name}``         ``GPL 2.0``
``$${license.spdx}``         ``GPL-2.0-or-later``
``$${license.header}``       <full copyright header>
``$${license.full}``         <full copyright file text>
``$${version}``              ``0.1``
``$${status.Name}``          ``Alpha``
``$${status.name}``          ``alpha``
``$${status.pypi}``          ``3 - Alpha``
``$${status.dunder}``        ``Development``
``$${status.Description}``   ``An alpha state``
``$${status.description}``   ``an alpha state``
``$${Description}``          ``My New Project``
``$${description}``          ``my new project``
``$${Description.}``         ``my new project.`` ['.' suffix if needed]
``$${authors}``              ``Joe Johnson, Kerri Ki``
``$${authors.list}``         ``["Joe Johnson", "Kerri Ki"]``
``$${keywords}``             ``python, fancy``
``$${keywords.list}``        ``["python", "fancy"]``
``$${tyranno.version}``      ``0.9.0``
=========================   ==================================
