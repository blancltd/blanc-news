# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glitter', '0001_initial'),
        ('blanc_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-date',), 'get_latest_by': 'date', 'permissions': (('edit_page', 'Can edit page'), ('publish_page', 'Can publish page'), ('view_protected_page', 'Can view protected page'))},
        ),
        migrations.AddField(
            model_name='post',
            name='current_version',
            field=models.ForeignKey(blank=True, editable=False, to='glitter.Version', null=True),
        ),
    ]
