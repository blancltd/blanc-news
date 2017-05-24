# -*- coding: utf-8 -*-

from django.utils import six

from .models import Post


class PostMixin(object):

    def get_queryset(self):
        queryset = Post.objects.published()

        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, six.string_types):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset

    def get_ordering(self):
        return '-is_sticky'
