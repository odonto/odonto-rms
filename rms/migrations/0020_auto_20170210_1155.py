# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rms', '0019_auto_20170201_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('on_medication', models.BooleanField(default=False, verbose_name=b'Currently On Medication')),
                ('medications_taken', models.TextField(blank=True)),
                ('created_by', models.ForeignKey(related_name='created_rms_medication_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_rms_medication_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.RenameField(
            model_name='xray',
            old_name='name',
            new_name='view',
        ),
        migrations.RemoveField(
            model_name='medicalissues',
            name='medications_taken',
        ),
        migrations.AddField(
            model_name='xray',
            name='xray_was_taken',
            field=models.NullBooleanField(verbose_name=b'An Xray Was Taken'),
        ),
        migrations.AlterField(
            model_name='carerdetails',
            name='address_line1',
            field=models.CharField(max_length=45, null=True, verbose_name=b'Address Line 1', blank=True),
        ),
        migrations.AlterField(
            model_name='carerdetails',
            name='address_line2',
            field=models.CharField(max_length=45, null=True, verbose_name=b'Address Line 2', blank=True),
        ),
        migrations.AlterField(
            model_name='disability',
            name='able_to_communicate',
            field=models.CharField(default=b'Unimpaired', choices=[(b'Unimpaired', b'Unimpaired'), (b'Partially Impaired', b'Partially Impaired'), (b'Severly Impaired', b'Severly Impaired')], max_length=256, blank=True, null=True, verbose_name=b'Unable To Communicate'),
        ),
        migrations.AlterField(
            model_name='disability',
            name='able_to_leave_home',
            field=models.BooleanField(default=False, verbose_name=b'Unable To Leave Home'),
        ),
        migrations.AlterField(
            model_name='disability',
            name='able_to_stand_for_transfer',
            field=models.BooleanField(default=False, verbose_name=b'Unable To Stand For Transfer'),
        ),
        migrations.AlterField(
            model_name='disability',
            name='has_capacity_to_consent',
            field=models.BooleanField(default=False, verbose_name=b'Doubts Over Capacity To Consent'),
        ),
        migrations.AlterField(
            model_name='medicalissues',
            name='has_medical_issues',
            field=models.BooleanField(default=False, verbose_name=b'Relevent Medical Issues We Should Know About'),
        ),
        migrations.AlterField(
            model_name='medicalissues',
            name='main_medical_conditions',
            field=models.TextField(verbose_name=b'Relevent Medical Issues', blank=True),
        ),
    ]
