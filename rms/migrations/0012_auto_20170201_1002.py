# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0011_auto_20170201_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allocatedclinic',
            name='location_fk',
        ),
        migrations.RemoveField(
            model_name='allocatedclinic',
            name='location_ft',
        ),
        migrations.AddField(
            model_name='allocatedclinic',
            name='location',
            field=models.ForeignKey(blank=True, to='rms.ClinicLocation', null=True),
        ),
    ]
