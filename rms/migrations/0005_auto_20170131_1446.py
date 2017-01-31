# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0027_auto_20170114_1302'),
        ('rms', '0004_disibility_medicalissues_mentalhealthissues_referraldetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('has_disability', models.BooleanField(default=False)),
                ('able_to_communicate', models.BooleanField(default=False)),
                ('able_to_leave_home', models.BooleanField(default=False)),
                ('able_to_stand_for_transfer', models.BooleanField(default=False)),
                ('has_capacity_to_consent', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(related_name='created_rms_disability_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_rms_disability_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.RemoveField(
            model_name='disibility',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='disibility',
            name='episode',
        ),
        migrations.RemoveField(
            model_name='disibility',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='Disibility',
        ),
    ]
