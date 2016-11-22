# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_controll', '0012_auto_20161028_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='adjustment',
            name='saldo_qty',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adjustment',
            name='adjustment_qty',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Quantity', blank=True),
        ),
        migrations.AlterField(
            model_name='issuedadjustment',
            name='issued_qty',
            field=models.PositiveIntegerField(default=1, verbose_name=b'Quantity', blank=True),
        ),
    ]
