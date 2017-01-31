# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0027_auto_20170114_1302'),
        ('rms', '0005_auto_20170131_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('address_line1', models.CharField(max_length=45, null=True, verbose_name=b'Address line 1', blank=True)),
                ('address_line2', models.CharField(max_length=45, null=True, verbose_name=b'Address line 2', blank=True)),
                ('city', models.CharField(max_length=50, blank=True)),
                ('county', models.CharField(max_length=40, null=True, verbose_name=b'County', blank=True)),
                ('post_code', models.CharField(max_length=10, null=True, verbose_name=b'Post Code', blank=True)),
                ('tel1', models.CharField(max_length=50, null=True, blank=True)),
                ('tel2', models.CharField(max_length=50, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_rms_contactdetails_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('updated_by', models.ForeignKey(related_name='updated_rms_contactdetails_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name_plural': 'Contact details',
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
    ]
