# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_controll', '0008_auto_20161018_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='gipo',
            name='status_rent',
            field=models.BooleanField(default=False),
        ),
    ]
