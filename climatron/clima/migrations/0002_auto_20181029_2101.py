# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-29 20:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clima', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendario',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='historico',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]