# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20150322_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='chan_id',
            field=models.CharField(help_text='The internal identifier for this channel.', unique=True, max_length=64, verbose_name='Channel ID'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='channel',
            name='stream_uri',
            field=models.CharField(default='', help_text='Full URI, including protocol. Supports http(s), rtmp, mms, hdhomerun, etc. See the <a href="https://github.com/MarconiMediaGroup/M3U8-Creator/wiki" target="_blank">wiki</a> for details.', max_length=256, verbose_name='Stream URI', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='channel',
            name='virtual_channel',
            field=models.IntegerField(default=0, help_text='Channel Number Assignment (Future Use. Ordering-only for now.)', verbose_name='Virtual Channel'),
            preserve_default=True,
        ),
    ]
