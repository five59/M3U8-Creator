# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150321_2159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='channel',
            options={'ordering': ['virtual_channel'], 'verbose_name': 'Channel', 'verbose_name_plural': 'Channels'},
        ),
    ]
