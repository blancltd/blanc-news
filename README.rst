===================
Django Glitter News
===================


Django glitter news for Django.


Installation
============


Getting the code
----------------

You can get **django-glitter-news** by using **pip**:

.. code-block:: console

    $ pip install django-glitter-news

Prerequisites
-------------

Make sure you add ``'glitter_news'``, ``'taggit'`` and ``'adminsortable'`` to your
``INSTALLED_APPS`` setting:

.. code-block:: python

    INSTALLED_APPS = [
        # ...
        'glitter_news',
        'taggit',
        'adminsortable',
        # ...
    ]

URLconf
-------

Add the Glitter News URLs to your project’s URLconf as follows:


.. code-block:: python

    url(r'^news/', include('glitter_news.urls', namespace='glitter-news'))


Configuration
=============

The following options can be set in your project's `settings.py`:

GLITTER_NEWS_TAGS
-----------------

This setting enables tags for the model ``Post`` in your project.

Default is ``False``.

Example:

.. code-block:: python
    GLITTER_NEWS_TAGS = True

NEWS_PER_PAGE
-------------

Set the number of news articles which will be displayed on a page.

Default is ``10``.

Example:

.. code-block:: python
    NEWS_PER_PAGE = 10

NEWS_NO_STICKY_ON_ALL
---------------------

Disable the sticky posts functionality when displaying the list of all news.

Default is ``False``.

Example:

.. code-block:: python
    NEWS_NO_STICKY_ON_ALL = True
