# -*- coding: utf-8 -*-

from django.contrib import admin

from blanc_pages.admin import BlancPageAdminMixin

from .models import Category, Post


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
            'fields': ('slug', 'published')
        }),
    )
    date_hierarchy = 'date'
    list_display = ('title', 'date', 'category', 'published')
    list_editable = ('published',)
    list_filter = ('published', 'date', 'category__title')
    prepopulated_fields = {
        'slug': ('title',)
    }
