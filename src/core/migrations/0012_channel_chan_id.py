# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20150321_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='chan_id',
            field=models.CharField(default='', help_text='The internal identifier for this channel', max_length=64, verbose_name='Channel ID'),
            preserve_default=True,
        ),
    ]
