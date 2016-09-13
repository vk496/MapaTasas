# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tasas.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasas', '0012_auto_20160306_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.IntegerField(blank=True, help_text='Curso académico', null=True)),
                ('email', models.EmailField(blank=True, help_text='Indica un correo electrónico si deseas que nos pongamos en contacto contigo', max_length=254, null=True)),
                ('descripcion', models.TextField(help_text='Describe el problema', max_length=100000)),
                ('universidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reportes', to='tasas.Universidad')),
            ],
        ),
    ]
