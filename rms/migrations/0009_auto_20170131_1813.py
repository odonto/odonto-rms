# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0008_auto_20170131_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliniclocation',
            name='address_line1',
            field=models.CharField(max_length=45, null=True, verbose_name=b'Address line 1', blank=True),
        ),
        migrations.AddField(
            model_name='cliniclocation',
            name='address_line2',
            field=models.CharField(max_length=45, null=True, verbose_name=b'Address line 2', blank=True),
        ),
        migrations.AddField(
            model_name='cliniclocation',
            name='post_code',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Post Code', blank=True),
        ),
        migrations.AddField(
            model_name='cliniclocation',
            name='tel',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliniclocation',
            name='tier',
            field=models.CharField(max_length=b'1', null=True, blank=True),
        ),
    ]
