# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_datosusuario_correo'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosusuario',
            name='qr',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]