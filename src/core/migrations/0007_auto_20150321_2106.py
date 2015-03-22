# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150321_2042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contenttype',
            options={'verbose_name': 'Content Type', 'verbose_name_plural': 'Content Types'},
        ),
        migrations.AddField(
            model_name='channel',
            name='virtual_channel',
            field=models.IntegerField(default=0, help_text='Channel Number Assignment', verbose_name='Virtual Channel'),
            preserve_default=True,
        ),
    ]
