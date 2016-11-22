# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_controll', '0010_auto_20161025_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grpo',
            options={'verbose_name': 'GRPO', 'verbose_name_plural': 'GRPO'},
        ),
        migrations.AlterField(
            model_name='item',
            name='item_qty',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
