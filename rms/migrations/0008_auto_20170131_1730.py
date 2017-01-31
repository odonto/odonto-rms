# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0007_auto_20170131_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='carerdetails',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contactdetails',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contactdetails',
            name='tel1',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Telephone No.', blank=True),
        ),
    ]
