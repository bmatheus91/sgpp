# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-23 12:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectindicator',
            name='indicator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicators.Indicator'),
        ),
        migrations.AlterField(
            model_name='projectindicatormonitor',
            name='indicator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicators.Indicator'),
        ),
        migrations.DeleteModel(
            name='Indicator',
        ),
    ]
