# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-29 20:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clima', '0005_auto_20181029_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historico',
            old_name='nombre_sensor',
            new_name='sensor',
        ),
    ]