# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0008_auto_20170131_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='referralreason',
            name='urgency',
            field=models.CharField(default=b'Routine', max_length=256, null=True, blank=True, choices=[(b'Urgent', b'Urgent'), (b'Routine', b'Routine')]),
        ),
        migrations.AlterField(
            model_name='disability',
            name='able_to_communicate',
            field=models.CharField(default=b'Unimpaired', choices=[(b'Unimpaired', b'Unimpaired'), (b'Partially impaired', b'Partially impaired'), (b'Severly impaired', b'Severly impaired')], max_length=256, blank=True, null=True, verbose_name=b'Unable to communicate'),
        ),
        migrations.AlterField(
            model_name='disability',
            name='able_to_leave_home',
            field=models.BooleanField(default=False, verbose_name=b'Unable to leave home'),
        ),
        migrations.AlterField(
            model_name='disability',
            name='able_to_stand_for_transfer',
            field=models.BooleanField(default=False, verbose_name=b'Unable to stand for transfer'),
        ),
        migrations.AlterField(
            model_name='disability',
            name='has_capacity_to_consent',
            field=models.BooleanField(default=False, verbose_name=b'Doubts over capacity to consent'),
        ),
    ]
