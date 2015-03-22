# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(default='', help_text='The user-friendly name to display in the UI.', max_length=128, verbose_name='Display Name', blank=True)),
                ('slug', models.CharField(default='', help_text='Channel name with spaces replaced with "_"\'s', max_length=64, verbose_name='Slug', blank=True)),
                ('chan_id', models.CharField(help_text='The value of "channel id" in the EPG xmltv file.', unique=True, max_length=64, verbose_name='XMLTV ID')),
                ('chan_order', models.IntegerField(default=0, verbose_name='Order')),
                ('logo_name', models.CharField(default='', help_text='The name of the channel logo without the .png extension.', max_length=64, verbose_name='Logo Filename', blank=True)),
                ('stream_uri', models.CharField(default='', help_text='Full URI, including protocol.', max_length=256, verbose_name='Stream URI', blank=True)),
            ],
            options={
                'verbose_name': 'Channel',
                'verbose_name_plural': 'Channels',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('iso2', models.CharField(max_length=2, unique=True, serialize=False, verbose_name='ISO2', primary_key=True)),
                ('name', models.CharField(max_length=96, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grouping',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Channel Group',
                'verbose_name_plural': 'Channel Groups',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='channel',
            name='country',
            field=models.ForeignKey(to='core.Country', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='channel',
            name='grouping',
            field=models.ForeignKey(to='core.Grouping', null=True),
            preserve_default=True,
        ),
    ]
