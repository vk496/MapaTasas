# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 13:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasas', '0011_auto_20160304_1826'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasa',
            options={'ordering': ['curso', 'tipo']},
        ),
    ]