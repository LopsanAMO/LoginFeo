# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 11:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datoshorario',
            name='user',
        ),
        migrations.RemoveField(
            model_name='datosmateria',
            name='horario',
        ),
        migrations.RemoveField(
            model_name='horas',
            name='materia',
        ),
        migrations.DeleteModel(
            name='datoshorario',
        ),
        migrations.DeleteModel(
            name='datosmateria',
        ),
        migrations.DeleteModel(
            name='horas',
        ),
    ]
