# -*- coding: utf-8 -*-

from django.contrib import admin
from django.core.urlresolvers import reverse

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
    list_filter = ('published', 'date', 'category')
    prepopulated_fields = {
        'slug': ('title',)
    }

    def admin_url(self, obj):
            info = self.model._meta.app_label, self.model._meta.model_name
            redirect_url = reverse('admin:%s_%s_redirect' % info, kwargs={'object_id': obj.id})
            return '<a href="%s">%s</a>' % (redirect_url, 'URL')
    admin_url.short_description = 'URL'
    admin_url.allow_tags = True

