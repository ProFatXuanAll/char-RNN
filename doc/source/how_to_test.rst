How To Test Guide
=================

.. note::

    You need to install dev tools first by running

    .. code-block:: sh

        pipenv install --dev

Test Style Guide
----------------

We use pytest_ testing framework to test our code.
We use coverage_ to provide test coverage report.
Please RTFM.

.. _pytest: https://docs.pytest.org/en/reorganize-docs/contents.html
.. _coverage: https://coverage.readthedocs.io/en/coverage-5.3/index.html

Run Test
--------

Run the following command in project root directory::

    pipenv run test

Generate Test Coverage Report
-----------------------------

Run the following command in project root directory::

    pipenv run test-coverage

.. todo::

    Add more test writing guideline.
