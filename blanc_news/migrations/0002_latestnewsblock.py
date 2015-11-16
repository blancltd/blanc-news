# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glitter', '0001_initial'),
        ('blanc_news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestNewsBlock',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('category', models.ForeignKey(null=True, blank=True, to='blanc_news.Category')),
                ('content_block', models.ForeignKey(null=True, editable=False, to='glitter.ContentBlock')),
            ],
            options={
                'verbose_name': 'latest news',
            },
        ),
    ]
