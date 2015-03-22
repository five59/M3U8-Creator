# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150320_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='channel',
            options={'ordering': ['order'], 'verbose_name': 'Channel', 'verbose_name_plural': 'Channels'},
        ),
        migrations.RemoveField(
            model_name='channel',
            name='chan_order',
        ),
        migrations.AddField(
            model_name='channel',
            name='order',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=True,
        ),
    ]
