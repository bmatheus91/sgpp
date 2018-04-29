# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-18 01:48
from __future__ import unicode_literals

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('forecast_finish_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Em Análise'), (2, 'Análise Realizada'), (3, 'Análise Aprovada'), (4, 'Iniciado'), (5, 'Planejado'), (6, 'Em Andamento'), (7, 'Encerrado'), (8, 'Cancelado')], default=1)),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, 'Baixo'), (2, 'Médio'), (3, 'Alto')])),
                ('modified', models.DateTimeField(auto_now=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectFollowUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_ups', to='projects.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectIndicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_value', models.PositiveIntegerField()),
                ('min_value', models.PositiveIntegerField()),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Indicator')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indicators', to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectIndicatorMonitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase', models.PositiveSmallIntegerField(choices=[(1, 'Iniciação'), (2, 'Planejamento'), (3, 'Execução'), (4, 'Finalização')])),
                ('value', models.PositiveIntegerField()),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Indicator')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indicator_monitor', to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectStatusMonitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Em Análise'), (2, 'Análise Realizada'), (3, 'Análise Aprovada'), (4, 'Iniciado'), (5, 'Planejado'), (6, 'Em Andamento'), (7, 'Encerrado'), (8, 'Cancelado')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_monitor', to='projects.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, unique=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='projects.Project')),
            ],
        ),
    ]
