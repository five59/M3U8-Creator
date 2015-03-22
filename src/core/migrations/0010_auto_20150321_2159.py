# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150321_2112'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='channel',
            options={'verbose_name': 'Channel', 'verbose_name_plural': 'Channels'},
        ),
        migrations.RemoveField(
            model_name='channel',
            name='order',
        ),
    ]
