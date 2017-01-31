# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0027_auto_20170114_1302'),
        ('rms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllocatedClinic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('confirmed', models.BooleanField()),
                ('location_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_rms_allocatedclinic_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ClinicLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='allocatedclinic',
            name='location_fk',
            field=models.ForeignKey(blank=True, to='rms.ClinicLocation', null=True),
        ),
        migrations.AddField(
            model_name='allocatedclinic',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_rms_allocatedclinic_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
