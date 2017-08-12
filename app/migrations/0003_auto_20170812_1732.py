# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170812_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sites',
            name='A_value',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sites',
            name='B_value',
            field=models.FloatField(),
        ),
    ]
