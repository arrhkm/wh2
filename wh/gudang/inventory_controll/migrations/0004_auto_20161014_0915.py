# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_controll', '0003_auto_20161013_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='grpo',
            name='status_po',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grnopo',
            name='bin_id',
            field=models.ForeignKey(verbose_name=b'Bin', blank=True, to='inventory_controll.Bin', null=True),
        ),
        migrations.AlterField(
            model_name='grnopo',
            name='date_create',
            field=models.DateField(auto_now_add=True, verbose_name=b'Date Create'),
        ),
        migrations.AlterField(
            model_name='grnopo',
            name='grnopo_qty',
            field=models.PositiveIntegerField(verbose_name=b'Quantity'),
        ),
        migrations.AlterField(
            model_name='grnopo',
            name='item_id',
            field=models.ForeignKey(verbose_name=b'Item', to='inventory_controll.Item'),
        ),
        migrations.AlterField(
            model_name='grnopo',
            name='loan_status',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Loan Status', blank=True),
        ),
        migrations.AlterField(
            model_name='grnopo',
            name='po_number',
            field=models.PositiveIntegerField(verbose_name=b'PO Number'),
        ),
        migrations.AlterField(
            model_name='grnopo',
            name='po_status',
            field=models.PositiveIntegerField(null=True, verbose_name=b'PO Status', blank=True),
        ),
        migrations.AlterField(
            model_name='grnopo',
            name='sales_order_phase_id',
            field=models.ForeignKey(verbose_name=b'Sales Order Phase', to='inventory_controll.SalesOrderPhase'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_number',
            field=models.PositiveIntegerField(serialize=False, verbose_name=b'Number', primary_key=True),
        ),
    ]
