# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_channel_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('slug', models.CharField(max_length=3, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Conent Type',
                'verbose_name_plural': 'Content Types',
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='channel',
            old_name='chan_id',
            new_name='xmltvid',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='slug',
        ),
        migrations.AddField(
            model_name='channel',
            name='content_type',
            field=models.ForeignKey(to='core.ContentType', null=True),
            preserve_default=True,
        ),
    ]
