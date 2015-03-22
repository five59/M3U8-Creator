# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150321_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('iso2', models.CharField(max_length=2, unique=True, serialize=False, verbose_name='ISO2', primary_key=True)),
                ('name', models.CharField(max_length=96, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Language',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='channel',
            name='primary_language',
            field=models.ForeignKey(to='core.Language', null=True),
            preserve_default=True,
        ),
    ]
