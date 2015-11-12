# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blanc_pages.assets.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
        ('glitter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('published', models.BooleanField(default=True, db_index=True)),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(unique_for_date='date', max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('date_url', models.DateField(db_index=True, editable=False)),
                ('summary', models.TextField(blank=True)),
                ('category', models.ForeignKey(to='blanc_news.Category')),
                ('current_version', models.ForeignKey(null=True, to='glitter.Version', blank=True, editable=False)),
                ('image', blanc_pages.assets.fields.AssetForeignKey(null=True, to='assets.Image', blank=True)),
            ],
            options={
                'get_latest_by': 'date',
                'ordering': ('-date',),
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'edit', 'publish'),
            },
        ),
    ]
