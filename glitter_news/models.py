# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django.utils import timezone

from taggit.managers import TaggableManager

from glitter.assets.fields import AssetForeignKey
from glitter.models import BaseBlock
from glitter.mixins import GlitterMixin


@python_2_unicode_compatible
class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('glitter-news:post-list-category', args=(self.slug,))


@python_2_unicode_compatible
class Post(GlitterMixin):
    title = models.CharField(max_length=100, db_index=True)
    category = models.ForeignKey('glitter_news.Category')
    author = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, unique_for_date='date')
    date = models.DateTimeField(default=timezone.now, db_index=True)
    # Is in used in overriding get_absolute_url method in case externals apps needs different URL.
    url = models.URLField(blank=True, editable=False)
    image = AssetForeignKey('glitter_assets.Image', null=True, blank=True)
    summary = models.TextField(blank=True)

    tags = TaggableManager(blank=True)

    class Meta(GlitterMixin.Meta):
        get_latest_by = 'date'
        ordering = ('-date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Get absolute url sometimes we assign external url to the post. """
        url = '/'
        if self.url:
            url = self.url
        else:
            params = {
                'year': self.date.year,
                'month': str(self.date.month).zfill(2),
                'day': str(self.date.day).zfill(2),
                'slug': self.slug,
            }
            url = reverse('glitter-news:post-detail', kwargs=params)
        return url


class LatestNewsBlock(BaseBlock):
    category = models.ForeignKey('glitter_news.Category', null=True, blank=True)

    class Meta:
        verbose_name = 'latest news'
