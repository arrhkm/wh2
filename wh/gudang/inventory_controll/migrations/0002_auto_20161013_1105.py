# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_controll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorderphase',
            name='phase_dscription',
            field=models.CharField(max_length=225, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='salesorderphase',
            name='phase_name',
            field=models.CharField(max_length=45, null=True, blank=True),
        ),
    ]
