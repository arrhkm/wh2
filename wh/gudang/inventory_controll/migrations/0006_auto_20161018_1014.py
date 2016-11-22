# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_controll', '0005_auto_20161014_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gipo',
            name='issued_number',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
        ),
    ]
