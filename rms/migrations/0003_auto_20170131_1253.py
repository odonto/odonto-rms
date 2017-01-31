# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0002_auto_20170131_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='allocatedclinic',
            name='letter_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='allocatedclinic',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
