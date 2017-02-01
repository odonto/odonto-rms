# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0027_auto_20170114_1302'),
        ('rms', '0009_auto_20170131_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='GPDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('tel', models.CharField(max_length=50, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_rms_gpdetails_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('updated_by', models.ForeignKey(related_name='updated_rms_gpdetails_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.AlterField(
            model_name='referralreason',
            name='urgency',
            field=models.CharField(default=b'Routine', max_length=256, null=True, blank=True, choices=[(b'Routine', b'Routine'), (b'Urgent', b'Urgent')]),
        ),
    ]
