# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_channel_chan_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='xmltvid',
            field=models.CharField(default='', help_text='The value of "channel id" in the EPG xmltv file.', max_length=64, verbose_name='XMLTV ID'),
            preserve_default=True,
        ),
    ]
