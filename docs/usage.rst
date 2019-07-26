=====
Usage
=====

To use appforsaladbar in a project, add it to your `INSTALLED_APPS`:

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
