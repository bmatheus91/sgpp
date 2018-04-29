# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-26 23:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0006_auto_20180426_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='leader',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='leader', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
