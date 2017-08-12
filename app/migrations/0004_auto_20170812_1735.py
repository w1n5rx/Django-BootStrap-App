# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170812_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sites',
            name='A_value',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='sites',
            name='B_value',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
    ]
