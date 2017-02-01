# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0017_xray_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xray',
            name='img',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
