# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_controll', '0011_auto_20161028_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_qty',
            field=models.PositiveIntegerField(default=0, null=True, blank=True),
        ),
    ]
