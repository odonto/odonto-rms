# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0022_remove_cliniclocation_tier'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliniclocation',
            name='address_line3',
            field=models.CharField(max_length=45, null=True, verbose_name=b'Address line 3', blank=True),
        ),
    ]
