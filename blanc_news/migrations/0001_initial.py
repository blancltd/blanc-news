# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import blanc_basic_assets.fields


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(max_length=100, unique_for_date='date')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
                ('date_url', models.DateField(editable=False, db_index=True)),
                ('teaser', models.TextField(blank=True)),
                ('content', models.TextField()),
                ('published', models.BooleanField(default=True, help_text='Post will be hidden unless this option is selected', db_index=True)),
            ],
            options={
                'ordering': ('-date',),
                'abstract': False,
                'get_latest_by': 'date',
                'swappable': 'NEWS_POST_MODEL',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=100)),
            ],
            options={
                'ordering': ('title',),
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(to='blanc_news.Category'),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=blanc_basic_assets.fields.AssetForeignKey(blank=True, to='assets.Image', null=True),
        ),
    ]
