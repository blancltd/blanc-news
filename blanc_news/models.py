# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

from blanc_basic_assets.fields import AssetForeignKey


@python_2_unicode_compatible
class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('title',)

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blanc-news:post-list-category', (), {'slug': self.slug})


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    category = models.ForeignKey('blanc_news.Category')
    slug = models.SlugField(max_length=100, unique_for_date='date')
    date = models.DateTimeField(default=timezone.now, db_index=True)
    date_url = models.DateField(db_index=True, editable=False)
    image = AssetForeignKey('assets.Image', null=True, blank=True)
    summary = models.TextField(blank=True)
    published = models.BooleanField(
        default=True,
        db_index=True,
        help_text='Post will be hidden unless this option is selected'
    )
    current_version = models.ForeignKey('glitter.Version', blank=True, null=True, editable=False)

    class Meta:
        get_latest_by = 'date'
        ordering = ('-date',)
        permissions = (
            ('edit_page', 'Can edit page'),
            ('publish_page', 'Can publish page'),
            ('view_protected_page', 'Can view protected page'),
        )

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blanc-news:post-detail', (), {
            'year': self.date_url.year,
            'month': str(self.date_url.month).zfill(2),
            'day': str(self.date_url.day).zfill(2),
            'slug': self.slug,
        })

    def save(self, *args, **kwargs):
        self.date_url = self.date.date()
        super(Post, self).save(*args, **kwargs)

