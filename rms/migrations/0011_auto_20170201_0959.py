# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0010_auto_20170131_1821'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliniclocation',
            options={},
        ),
        migrations.AlterField(
            model_name='cliniclocation',
            name='name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
