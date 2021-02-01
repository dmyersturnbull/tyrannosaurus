Testing database-connected code
=================================

Getting GitHub actions and Tox to work well with databases takes a little extra work.
This shows how to get MariaDB/MySQL working. The principles should be the same for other databases, like PostgreSQL.
`This project <https://github.com/dmyersturnbull/valarpy>`_ has a working example of this.

First, include MariaDB as a service by adding this under ``jobs`` in
``.github/workflows/commit.yml`` and ``.github/workflows/pull.yml``.
Note that the ``MYSQL_DATABASE: test`` does not refer to your database.

.. code-block::

        services:
            mysql:
                image: mariadb:latest
                env:
                    MYSQL_ROOT_PASSWORD: root
                    MYSQL_DATABASE: test
                ports:
                    - 3306:3306
                options: \
                    --health-cmd="mysqladmin ping" \
                    --health-interval=10s \
                    --health-timeout=5s \
                    --health-retries=3


Then, add a step to test the MariaDB connection. Add it before other steps so the workflow fails early.

.. code-block::

    -
        name: Initialize MariaDB
        run: |
            mysqladmin --host=127.0.0.1 ping


Then, add the SQL schema and rows needed for the tests to ``tests/resources/testdb.sql``.
There’s no security relevance here, so we can just use the root throughout.


.. warning::

    Make sure the name of your test database won’t ever conflict with a real database.
    Otherwise, you’ll lose your database.

Then, in ``tox.ini``, ``mysql`` to ``whitelist_externals``.
Then add this to the ``commands``. It’s likely to be fast, so consider adding it as the first step.

.. code-block::

    mysql -e 'SOURCE tests/resources/testdb.sql;' --host=127.0.0.1 --user=root --password=root

Oddly, the ``-host=127.0.0.1`` is important; "localhost" or leaving it as default won’t work.
You may also want to execute a ``DROP DATABASE`` query as the last command, but that may not be needed.

Your SQL file might start with something like:

.. code-block::

    DROP DATABASE IF EXISTS myfakedatabase;
    CREATE DATABASE myfakedatabase CHARACTER SET = 'utf8mb4' COLLATE 'utf8mb4_unicode_520_ci';
    DROP USER IF EXISTS 'myfakeuser'@'localhost';
    CREATE USER 'myfakedatabase'@'localhost' IDENTIFIED BY 'fakeuser123';
    GRANT SELECT, INSERT, UPDATE, DELETE ON myfakedatabase.* TO 'myfakeuser'@'localhost';
    USE valartest;

The SQL is executed using the root user, but your code may expect something different.
