# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0007_auto_20170131_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliniclocation',
            name='tier',
            field=models.CharField(default=2, max_length=b'1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactdetails',
            name='tel1',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Telephone No.', blank=True),
        ),
    ]
