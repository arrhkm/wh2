# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_controll', '0009_gipo_status_rent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adjustment',
            options={'verbose_name': 'Adjustment', 'verbose_name_plural': 'Adjustment'},
        ),
        migrations.AlterModelOptions(
            name='gipo',
            options={'verbose_name': 'Good Issued By PO', 'verbose_name_plural': 'Good Issued By PO'},
        ),
        migrations.AlterModelOptions(
            name='issuedadjustment',
            options={'verbose_name': 'Issued Adjustment', 'verbose_name_plural': 'Issued Adjustment'},
        ),
        migrations.AlterModelOptions(
            name='itemattributes',
            options={'verbose_name': 'Item Attribute', 'verbose_name_plural': 'Item Attribute'},
        ),
        migrations.AlterModelOptions(
            name='itemcategory',
            options={'verbose_name': 'Item Category', 'verbose_name_plural': 'Item Categories'},
        ),
        migrations.AlterModelOptions(
            name='itemregister',
            options={'verbose_name': 'Item Register', 'verbose_name_plural': 'Item Registers'},
        ),
        migrations.AddField(
            model_name='grpo',
            name='saldo_qty',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='adjustment',
            name='adjustment_actived',
            field=models.PositiveIntegerField(default=1, verbose_name=b'Status', choices=[(1, b'ACTIVE'), (0, b'CLOSED')]),
        ),
        migrations.AlterField(
            model_name='adjustment',
            name='adjustment_qty',
            field=models.PositiveIntegerField(verbose_name=b'Quantity'),
        ),
        migrations.AlterField(
            model_name='adjustment',
            name='bin_id',
            field=models.ForeignKey(verbose_name=b'Bin', blank=True, to='inventory_controll.Bin', null=True),
        ),
        migrations.AlterField(
            model_name='adjustment',
            name='date_created',
            field=models.DateField(auto_now_add=True, verbose_name=b'Date Created'),
        ),
        migrations.AlterField(
            model_name='adjustment',
            name='dscription',
            field=models.CharField(max_length=225, null=True, verbose_name=b'Description', blank=True),
        ),
        migrations.AlterField(
            model_name='adjustment',
            name='item_id',
            field=models.ForeignKey(verbose_name=b'Item', to='inventory_controll.Item'),
        ),
        migrations.AlterField(
            model_name='bin',
            name='name_location',
            field=models.CharField(max_length=45, verbose_name=b'Location Name'),
        ),
        migrations.AlterField(
            model_name='gipo',
            name='date_create',
            field=models.DateField(verbose_name=b'Date Created'),
        ),
        migrations.AlterField(
            model_name='gipo',
            name='dscription',
            field=models.CharField(max_length=225, null=True, verbose_name=b'Description', blank=True),
        ),
        migrations.AlterField(
            model_name='gipo',
            name='good_issued_type_id',
            field=models.ForeignKey(verbose_name=b'Good Issued Type', to='inventory_controll.GoodIssuedType'),
        ),
        migrations.AlterField(
            model_name='gipo',
            name='issued_number',
            field=models.CharField(max_length=20, serialize=False, verbose_name=b'Issued Number', primary_key=True),
        ),
        migrations.AlterField(
            model_name='gipo',
            name='qty_issued',
            field=models.PositiveIntegerField(verbose_name=b'Quantity'),
        ),
        migrations.AlterField(
            model_name='gipo',
            name='received_by',
            field=models.CharField(max_length=45, null=True, verbose_name=b'Received by', blank=True),
        ),
        migrations.AlterField(
            model_name='gipo',
            name='sent_location',
            field=models.CharField(max_length=45, null=True, verbose_name=b'Sent Location', blank=True),
        ),
        migrations.AlterField(
            model_name='goodissuedtype',
            name='good_issued_name',
            field=models.CharField(max_length=45, verbose_name=b'Good Issued Name'),
        ),
        migrations.AlterField(
            model_name='grpo',
            name='grpo_qty',
            field=models.PositiveIntegerField(verbose_name=b'Quantity'),
        ),
        migrations.AlterField(
            model_name='issuedadjustment',
            name='adjustment_id',
            field=models.ForeignKey(verbose_name=b'Adjustment', to='inventory_controll.Adjustment'),
        ),
        migrations.AlterField(
            model_name='issuedadjustment',
            name='issued_date',
            field=models.DateField(auto_now_add=True, verbose_name=b'Issued Date'),
        ),
        migrations.AlterField(
            model_name='issuedadjustment',
            name='issued_qty',
            field=models.PositiveIntegerField(verbose_name=b'Quantity'),
        ),
        migrations.AlterField(
            model_name='issuedadjustment',
            name='sales_order_phase_id',
            field=models.ForeignKey(verbose_name=b'Sales Order Phase', to='inventory_controll.SalesOrderPhase'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_qty',
            field=models.PositiveIntegerField(null=True, verbose_name=b'Quantity', blank=True),
        ),
    ]
