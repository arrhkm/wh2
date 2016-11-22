# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_controll', '0006_auto_20161018_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ginopo',
            name='grnopo_id',
        ),
        migrations.RemoveField(
            model_name='grnopo',
            name='bin_id',
        ),
        migrations.RemoveField(
            model_name='grnopo',
            name='item_id',
        ),
        migrations.RemoveField(
            model_name='grnopo',
            name='sales_order_phase_id',
        ),
        migrations.AlterUniqueTogether(
            name='issuednopovalue',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='issuednopovalue',
            name='ginopo_id',
        ),
        migrations.RemoveField(
            model_name='issuednopovalue',
            name='good_issued_type_id',
        ),
        migrations.RemoveField(
            model_name='issuednopovalue',
            name='sales_order_phase_id',
        ),
        migrations.RemoveField(
            model_name='issuedpovalue',
            name='gipo_id',
        ),
        migrations.RemoveField(
            model_name='issuedpovalue',
            name='goodissuedtype_id',
        ),
        migrations.RemoveField(
            model_name='issuedpovalue',
            name='sales_order_phase_id',
        ),
        migrations.AddField(
            model_name='gipo',
            name='good_issued_type_id',
            field=models.ForeignKey(default=1, to='inventory_controll.GoodIssuedType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gipo',
            name='sales_order_phase_id',
            field=models.ForeignKey(db_column=b'sales_order_phase_id', blank=True, to='inventory_controll.SalesOrderPhase', null=True),
        ),
        migrations.DeleteModel(
            name='GiNoPo',
        ),
        migrations.DeleteModel(
            name='GrNoPo',
        ),
        migrations.DeleteModel(
            name='IssuedNoPoValue',
        ),
        migrations.DeleteModel(
            name='IssuedPoValue',
        ),
    ]
