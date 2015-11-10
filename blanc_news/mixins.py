# -*- coding: utf-8 -*-

from .models import Post


class PostMixin(object):
    def get_queryset(self):
        return Post.objects.select_related().filter(published=True).exclude(current_version=None)
