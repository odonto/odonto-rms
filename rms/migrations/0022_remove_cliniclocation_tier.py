# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0021_auto_20170210_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliniclocation',
            name='tier',
        ),
    ]
