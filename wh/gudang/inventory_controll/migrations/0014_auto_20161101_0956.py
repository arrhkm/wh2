# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_controll', '0013_auto_20161101_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjustment',
            name='saldo_qty',
            field=models.PositiveIntegerField(default=0, blank=True),
        ),
    ]
