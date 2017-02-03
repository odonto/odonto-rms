# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0018_auto_20170201_1359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allocatedclinic',
            options={'permissions': (('can_assign_location', 'Can assign a location'), ('can_confirm_location', 'Can confirm a location'))},
        ),
        migrations.AlterModelOptions(
            name='referralreason',
            options={'permissions': (('can_refer', 'Can refer a patient'),)},
        ),
    ]
