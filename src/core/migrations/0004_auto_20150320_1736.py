# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150320_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='logo',
            field=models.FileField(help_text='Image in PNG format. Should be square, at least 256x256.', upload_to=core.models.logo_filename, null=True, verbose_name='Logo', blank=True),
            preserve_default=True,
        ),
    ]
