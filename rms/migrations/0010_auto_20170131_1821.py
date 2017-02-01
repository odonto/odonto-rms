# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0009_auto_20170131_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliniclocation',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
