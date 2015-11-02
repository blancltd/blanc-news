# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import blanc_basic_assets.fields


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
        ('glitter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=100)),
            ],
            options={
                'ordering': ('title',),
                'abstract': False,
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(max_length=100, unique_for_date=b'date')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('date_url', models.DateField(editable=False, db_index=True)),
                ('teaser', models.TextField(blank=True)),
                ('published', models.BooleanField(default=True, help_text=b'Post will be hidden unless this option is selected', db_index=True)),
                ('category', models.ForeignKey(to='blanc_news.Category')),
                ('current_version', models.ForeignKey(blank=True, editable=False, to='glitter.Version', null=True)),
                ('image', blanc_basic_assets.fields.AssetForeignKey(blank=True, to='assets.Image', null=True)),
            ],
            options={
                'ordering': ('-date',),
                'abstract': False,
                'get_latest_by': 'date',
                'permissions': (('edit_page', 'Can edit page'), ('publish_page', 'Can publish page'), ('view_protected_page', 'Can view protected page')),
            },
        ),
    ]
