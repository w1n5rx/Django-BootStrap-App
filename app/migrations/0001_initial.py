# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_value', models.DateField()),
                ('A_value', models.FloatField()),
                ('B_value', models.FloatField()),
                ('site_name', models.CharField(max_length=30)),
            ],
        ),
    ]
