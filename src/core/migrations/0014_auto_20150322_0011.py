# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20150322_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='chan_id',
            field=models.CharField(help_text='The internal identifier for this channel', unique=True, max_length=64, verbose_name='Channel ID'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='channel',
            name='xmltvid',
            field=models.CharField(default='', help_text='The value of "channel id" in the EPG xmltv file.', max_length=64, verbose_name='XMLTV ID', blank=True),
            preserve_default=True,
        ),
    ]
