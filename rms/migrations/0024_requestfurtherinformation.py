# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rms', '0023_cliniclocation_address_line3'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestFurtherInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('information_required', models.TextField(null=True, blank=True)),
                ('completed', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(related_name='created_rms_requestfurtherinformation_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_rms_requestfurtherinformation_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
    ]
