# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-25 14:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0002_auto_20180423_1002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indicator',
            old_name='active',
            new_name='is_active',
        ),
    ]