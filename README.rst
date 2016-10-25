===================
Django Glitter News
===================


Django glitter news for Django.


Getting Started
===============

Make sure you add ``'taggit'`` to your ``INSTALLED_APPS`` setting:

.. code-block:: python

    INSTALLED_APPS = [
        # ...
        'taggit',
        # ...
    ]


Configuration
=============

The django-glitter-news provides just one setting that you can enable in your 
project.

GLITTER_NEWS_TAGS
-----------------

Default: ``False``

This setting enables tags for the model ``Post`` in your project.
