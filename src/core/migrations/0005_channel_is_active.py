# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150320_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Should this channel be displayed?', verbose_name='Active?'),
            preserve_default=True,
        ),
    ]
