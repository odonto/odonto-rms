# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0016_auto_20170201_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='xray',
            name='name',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
    ]
