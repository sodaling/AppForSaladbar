=============================
appforsaladbar
=============================

.. image:: https://badge.fury.io/py/AppForSaladbar.svg
    :target: https://badge.fury.io/py/AppForSaladbar

.. image:: https://travis-ci.org/sodaling/AppForSaladbar.svg?branch=master
    :target: https://travis-ci.org/sodaling/AppForSaladbar

.. image:: https://codecov.io/gh/sodaling/AppForSaladbar/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/sodaling/AppForSaladbar

Your project description goes here

Documentation
-------------

The full documentation is at https://AppForSaladbar.readthedocs.io.

Quickstart
----------

Install appforsaladbar::

    pip install AppForSaladbar

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'appforsaladbar.apps.AppforsaladbarConfig',
        ...
    )

Add appforsaladbar's URL patterns:

.. code-block:: python

    from appforsaladbar import urls as appforsaladbar_urls


    urlpatterns = [
        ...
        url(r'^', include(appforsaladbar_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
