# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='logo_name',
        ),
        migrations.AddField(
            model_name='channel',
            name='logo',
            field=models.FileField(help_text='Image in PNG format. Should be square, at least 256x256.', upload_to=core.models.logo_filename, null=True, verbose_name='Logo'),
            preserve_default=True,
        ),
    ]
