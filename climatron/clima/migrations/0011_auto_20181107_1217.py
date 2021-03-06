# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-07 11:17
from __future__ import unicode_literals

import datetime
from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clima', '0010_estado_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='historico_instalacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('valor', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=5)),
                ('estado', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='clima.estado')),
            ],
            options={
                'verbose_name_plural': 'Historicos_Sensores',
            },
        ),
        migrations.AddField(
            model_name='sensor',
            name='fecha_lectura',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='sensor_instalacion',
            name='fecha_lectura',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='sensor_instalacion',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=5),
        ),
        migrations.AlterField(
            model_name='historico',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='historico_instalacion',
            name='nombre_sensor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='clima.sensor_instalacion'),
        ),
    ]
