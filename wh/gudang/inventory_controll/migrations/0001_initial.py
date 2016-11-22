# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adjustment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('dscription', models.CharField(max_length=225, null=True, blank=True)),
                ('adjustment_qty', models.PositiveIntegerField()),
                ('adjustment_actived', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_location', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='GiNoPo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_create', models.DateField(auto_now_add=True)),
                ('ginopo_qty', models.PositiveIntegerField()),
                ('dscription', models.CharField(max_length=225)),
                ('received_by', models.CharField(max_length=45)),
                ('sent_location', models.CharField(max_length=45)),
                ('status', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GiPo',
            fields=[
                ('issued_number', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('date_create', models.DateField()),
                ('dscription', models.CharField(max_length=225)),
                ('qty_issued', models.PositiveIntegerField()),
                ('received_by', models.CharField(max_length=45)),
                ('sent_location', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='GoodIssuedType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('good_issued_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='GrNoPo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_create', models.DateField(auto_now_add=True)),
                ('po_number', models.PositiveIntegerField()),
                ('grnopo_qty', models.PositiveIntegerField()),
                ('po_status', models.PositiveIntegerField(null=True, blank=True)),
                ('loan_status', models.PositiveIntegerField(null=True, blank=True)),
                ('bin_id', models.ForeignKey(blank=True, to='inventory_controll.Bin', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GrPo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_create', models.DateField(auto_now_add=True, verbose_name=b'Date Created')),
                ('grpo_qty', models.DecimalField(verbose_name=b'Quantity', max_digits=12, decimal_places=2)),
                ('bin_id', models.ForeignKey(verbose_name=b'Bin', blank=True, to='inventory_controll.Bin', null=True)),
            ],
            options={
                'verbose_name': 'Good Received with PO',
                'verbose_name_plural': 'Good Received with PO',
            },
        ),
        migrations.CreateModel(
            name='IssuedAdjustment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issued_date', models.DateField(auto_now_add=True)),
                ('issued_qty', models.PositiveIntegerField()),
                ('adjustment_id', models.ForeignKey(to='inventory_controll.Adjustment')),
            ],
        ),
        migrations.CreateModel(
            name='IssuedNoPoValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('posted_status', models.PositiveIntegerField(null=True, blank=True)),
                ('ginopo_id', models.ForeignKey(to='inventory_controll.GiNoPo')),
                ('good_issued_type_id', models.ForeignKey(to='inventory_controll.GoodIssuedType')),
            ],
        ),
        migrations.CreateModel(
            name='IssuedPoValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('loan_status', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('gipo_id', models.ForeignKey(to='inventory_controll.GiPo', db_column=b'gipo_id')),
                ('goodissuedtype_id', models.ForeignKey(to='inventory_controll.GoodIssuedType', db_column=b'goodissuedtype_id')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('code', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('item_name', models.CharField(max_length=255, verbose_name=b'Item Name')),
                ('item_qty', models.DecimalField(null=True, verbose_name=b'Quantity Stock', max_digits=12, decimal_places=2, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemAttributes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attr_name', models.CharField(max_length=45, verbose_name=b'Item Measurement Attributes')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_category_name', models.CharField(max_length=45, verbose_name=b'Category Name')),
            ],
        ),
        migrations.CreateModel(
            name='ItemRegister',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_reg', models.CharField(max_length=45, verbose_name=b'Code')),
                ('name_reg', models.CharField(max_length=45, verbose_name=b'Register Name')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('po_number', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('supplier_name', models.CharField(max_length=45, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('so_number', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('so_name', models.CharField(max_length=45)),
                ('so_dscription', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='SalesOrderPhase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phase_number', models.PositiveIntegerField()),
                ('phase_name', models.CharField(max_length=45)),
                ('phase_dscription', models.CharField(max_length=225)),
                ('sales_order', models.ForeignKey(to='inventory_controll.SalesOrder')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='item_attribute',
            field=models.ForeignKey(default=None, blank=True, to='inventory_controll.ItemAttributes', null=True, verbose_name=b'ItemAttributes'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_category',
            field=models.ForeignKey(default=None, blank=True, to='inventory_controll.ItemCategory', null=True, verbose_name=b'Category'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_register',
            field=models.ForeignKey(default=None, blank=True, to='inventory_controll.ItemRegister', null=True, verbose_name=b'SAP Registered'),
        ),
        migrations.AddField(
            model_name='issuedpovalue',
            name='sales_order_phase_id',
            field=models.ForeignKey(to='inventory_controll.SalesOrderPhase', db_column=b'sales_order_phase_id'),
        ),
        migrations.AddField(
            model_name='issuednopovalue',
            name='sales_order_phase_id',
            field=models.ForeignKey(to='inventory_controll.SalesOrderPhase'),
        ),
        migrations.AddField(
            model_name='issuedadjustment',
            name='sales_order_phase_id',
            field=models.ForeignKey(to='inventory_controll.SalesOrderPhase'),
        ),
        migrations.AddField(
            model_name='grpo',
            name='item_code',
            field=models.ForeignKey(related_name='good_received_po', db_column=b'item_code', verbose_name=b'Item', to='inventory_controll.Item'),
        ),
        migrations.AddField(
            model_name='grpo',
            name='po_number',
            field=models.ForeignKey(db_column=b'po_number', verbose_name=b'Purchase Order', to='inventory_controll.PurchaseOrder'),
        ),
        migrations.AddField(
            model_name='grpo',
            name='sales_order_phase_id',
            field=models.ForeignKey(db_column=b'sales_order_phase_id', verbose_name=b'Sales Order', to='inventory_controll.SalesOrderPhase'),
        ),
        migrations.AddField(
            model_name='grnopo',
            name='item_id',
            field=models.ForeignKey(to='inventory_controll.Item'),
        ),
        migrations.AddField(
            model_name='grnopo',
            name='sales_order_phase_id',
            field=models.ForeignKey(to='inventory_controll.SalesOrderPhase'),
        ),
        migrations.AddField(
            model_name='gipo',
            name='grpo_id',
            field=models.ForeignKey(related_name='good_issued_po', db_column=b'grpo_id', to='inventory_controll.GrPo'),
        ),
        migrations.AddField(
            model_name='ginopo',
            name='grnopo_id',
            field=models.ForeignKey(to='inventory_controll.GrNoPo', db_column=b'grnopo_id'),
        ),
        migrations.AddField(
            model_name='adjustment',
            name='bin_id',
            field=models.ForeignKey(blank=True, to='inventory_controll.Bin', null=True),
        ),
        migrations.AddField(
            model_name='adjustment',
            name='item_id',
            field=models.ForeignKey(to='inventory_controll.Item'),
        ),
        migrations.AlterUniqueTogether(
            name='issuednopovalue',
            unique_together=set([('sales_order_phase_id', 'ginopo_id', 'good_issued_type_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='grpo',
            unique_together=set([('po_number', 'item_code', 'sales_order_phase_id')]),
        ),
    ]
