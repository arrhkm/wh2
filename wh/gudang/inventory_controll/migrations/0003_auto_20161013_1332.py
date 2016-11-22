# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_controll', '0002_auto_20161013_1105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Item', 'verbose_name_plural': 'Items'},
        ),
        migrations.AlterModelOptions(
            name='itemattributes',
            options={'verbose_name': 'Attributes', 'verbose_name_plural': 'Attributes'},
        ),
        migrations.AlterModelOptions(
            name='itemcategory',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='itemregister',
            options={'verbose_name': 'Register', 'verbose_name_plural': 'Registers'},
        ),
        migrations.AlterModelOptions(
            name='purchaseorder',
            options={'verbose_name': 'Purchase Order', 'verbose_name_plural': 'Purchase Order List'},
        ),
        migrations.AlterModelOptions(
            name='salesorder',
            options={'verbose_name': 'Sales Order', 'verbose_name_plural': 'Sales Orders'},
        ),
        migrations.AlterModelOptions(
            name='salesorderphase',
            options={'verbose_name': 'Sales Order Phase', 'verbose_name_plural': 'Sales Order Phases'},
        ),
        migrations.AlterField(
            model_name='item',
            name='code',
            field=models.CharField(max_length=20, serialize=False, verbose_name=b'Code', primary_key=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_attribute',
            field=models.ForeignKey(default=None, blank=True, to='inventory_controll.ItemAttributes', null=True, verbose_name=b'Attributes'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=255, verbose_name=b'Name'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_qty',
            field=models.DecimalField(null=True, verbose_name=b'Quantity', max_digits=12, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_register',
            field=models.ForeignKey(default=None, blank=True, to='inventory_controll.ItemRegister', null=True, verbose_name=b'Register'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_number',
            field=models.CharField(max_length=11, serialize=False, verbose_name=b'Number', primary_key=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='supplier_name',
            field=models.CharField(max_length=45, null=True, verbose_name=b'Supplier', blank=True),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='so_dscription',
            field=models.CharField(max_length=225, verbose_name=b'Description'),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='so_name',
            field=models.CharField(max_length=45, verbose_name=b'Name'),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='so_number',
            field=models.PositiveIntegerField(serialize=False, verbose_name=b'Number', primary_key=True),
        ),
        migrations.AlterField(
            model_name='salesorderphase',
            name='phase_dscription',
            field=models.CharField(max_length=225, null=True, verbose_name=b'Description', blank=True),
        ),
        migrations.AlterField(
            model_name='salesorderphase',
            name='phase_name',
            field=models.CharField(max_length=45, null=True, verbose_name=b'Name', blank=True),
        ),
        migrations.AlterField(
            model_name='salesorderphase',
            name='phase_number',
            field=models.PositiveIntegerField(verbose_name=b'Phase Number'),
        ),
        migrations.AlterField(
            model_name='salesorderphase',
            name='sales_order',
            field=models.ForeignKey(verbose_name=b'Sales Order', to='inventory_controll.SalesOrder'),
        ),
    ]
