# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20150322_0011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel',
            old_name='xmltvid',
            new_name='xmltv_id',
        ),
        migrations.AddField(
            model_name='channel',
            name='xmltv_name',
            field=models.CharField(default='', help_text='The value in the XMLTV file for display-name.', max_length=64, verbose_name='XMLTV Name', blank=True),
            preserve_default=True,
        ),
    ]
