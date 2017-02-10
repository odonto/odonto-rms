# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0020_auto_20170210_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='allocatedclinic',
            name='tier',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3')]),
        ),
        migrations.AddField(
            model_name='cliniclocation',
            name='fax',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cliniclocation',
            name='hoist_available',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cliniclocation',
            name='inhalation_sedation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cliniclocation',
            name='patient_transport',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cliniclocation',
            name='wheelchair_access',
            field=models.BooleanField(default=False),
        ),
    ]
