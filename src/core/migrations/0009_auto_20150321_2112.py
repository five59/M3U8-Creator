# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150321_2108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ['iso2'], 'verbose_name': 'Country', 'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='grouping',
            options={'ordering': ['name'], 'verbose_name': 'Channel Group', 'verbose_name_plural': 'Channel Groups'},
        ),
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['iso2'], 'verbose_name': 'Language', 'verbose_name_plural': 'Languages'},
        ),
        migrations.RenameField(
            model_name='channel',
            old_name='primary_language',
            new_name='language',
        ),
    ]
