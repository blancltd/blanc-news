# -*- coding: utf-8 -*-

from django.apps import apps as django_apps
from django.core.exceptions import ImproperlyConfigured


default_app_config = 'blanc_news.apps.BlancNewsConfig'


def get_post_model():
    try:
        return django_apps.get_model('blanc_news.Post')
    except ValueError:
        raise ImproperlyConfigured(
            "Blanc news  must be of the form 'app_label.model_name'"
        )
