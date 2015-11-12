# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django.utils import timezone

from blanc_pages.assets.fields import AssetForeignKey
from blanc_pages.mixins import GlitterMixin


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
        return reverse('blanc-news:post-list-category', args=(self.slug,))


@python_2_unicode_compatible
class Post(GlitterMixin):
    title = models.CharField(max_length=100, db_index=True)
    category = models.ForeignKey('blanc_news.Category')
    slug = models.SlugField(max_length=100, unique_for_date='date')
    date = models.DateTimeField(default=timezone.now, db_index=True)
    date_url = models.DateField(db_index=True, editable=False)
    image = AssetForeignKey('assets.Image', null=True, blank=True)
    summary = models.TextField(blank=True)

    class Meta(GlitterMixin.Meta):
        get_latest_by = 'date'
        ordering = ('-date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        params = {
            'year': self.date_url.year,
            'month': str(self.date_url.month).zfill(2),
            'day': str(self.date_url.day).zfill(2),
            'slug': self.slug,
        }
        return reverse('blanc-news:post-detail', kwargs=params)

    def save(self, *args, **kwargs):
        self.date_url = self.date.date()
        super(Post, self).save(*args, **kwargs)
