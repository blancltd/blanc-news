# -*- coding: utf-8 -*-

from django.contrib import admin

from blanc_pages import block_admin
from blanc_pages.admin import BlancPageAdminMixin, BlancPagePublishedFilter

from .models import Category, LatestNewsBlock, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(Post)
class PostAdmin(BlancPageAdminMixin, admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'category', 'date', 'image', 'summary',)
        }),
        ('Advanced options', {
            'fields': ('slug',)
        }),
    )
    date_hierarchy = 'date'
    list_display = ('title', 'date', 'category', 'is_published')
    list_filter = (BlancPagePublishedFilter, 'date', 'category')
    prepopulated_fields = {
        'slug': ('title',)
    }


block_admin.site.register(LatestNewsBlock)
block_admin.site.register_block(LatestNewsBlock, 'News')
