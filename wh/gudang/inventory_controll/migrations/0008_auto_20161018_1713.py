# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_controll', '0007_auto_20161018_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='gipo',
            name='grpo_id2',
            field=models.ForeignKey(related_name='gr_po_issued2', db_column=b'grpo_id2', blank=True, to='inventory_controll.GrPo', null=True),
        ),
        migrations.AddField(
            model_name='gipo',
            name='so_phase2',
            field=models.ForeignKey(related_name='so_phase_issued2', db_column=b'so_phase2', blank=True, to='inventory_controll.SalesOrderPhase', null=True),
        ),
        migrations.AlterField(
            model_name='gipo',
            name='dscription',
            field=models.CharField(max_length=225, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='gipo',
            name='received_by',
            field=models.CharField(max_length=45, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='gipo',
            name='sent_location',
            field=models.CharField(max_length=45, null=True, blank=True),
        ),
    ]
