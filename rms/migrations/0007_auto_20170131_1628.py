# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import opal.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0027_auto_20170114_1302'),
        ('rms', '0006_contactdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarerDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('surname', models.CharField(max_length=255, blank=True)),
                ('first_name', models.CharField(max_length=255, blank=True)),
                ('address_line1', models.CharField(max_length=45, null=True, verbose_name=b'Address line 1', blank=True)),
                ('address_line2', models.CharField(max_length=45, null=True, verbose_name=b'Address line 2', blank=True)),
                ('post_code', models.CharField(max_length=10, null=True, verbose_name=b'Post Code', blank=True)),
                ('tel', models.CharField(max_length=50, null=True, blank=True)),
                ('relationship_to_patient_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_rms_carerdetails_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ReferralReason',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('dental_treatment_needed', models.TextField()),
                ('dental_treatment_already_provided', models.TextField()),
                ('difficulties_encountered', models.TextField()),
                ('created_by', models.ForeignKey(related_name='created_rms_referralreason_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_rms_referralreason_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RelationshipToPatient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='disability',
            name='able_to_communicate',
            field=models.CharField(default=b'Unimpaired', max_length=256, null=True, blank=True, choices=[(b'Unimpaired', b'Unimpaired'), (b'partially impaired', b'partially impaired'), (b'severly impaired', b'severly impaired')]),
        ),
        migrations.AddField(
            model_name='carerdetails',
            name='relationship_to_patient_fk',
            field=models.ForeignKey(blank=True, to='rms.RelationshipToPatient', null=True),
        ),
        migrations.AddField(
            model_name='carerdetails',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_rms_carerdetails_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
