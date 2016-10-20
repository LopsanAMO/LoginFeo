# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 11:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='alarmaexamen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_alarmaexamen', models.CharField(max_length=100)),
                ('fecha_entrega', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='examen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_examen', models.CharField(max_length=100)),
                ('id_tarea', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_entrega', models.DateTimeField()),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materia.datosmateria')),
            ],
        ),
        migrations.CreateModel(
            name='repeticionexamen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horaexamen', models.DateTimeField()),
                ('id_alarmaexamen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examen.alarmaexamen')),
            ],
        ),
        migrations.AddField(
            model_name='alarmaexamen',
            name='id_examen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examen.examen'),
        ),
    ]
