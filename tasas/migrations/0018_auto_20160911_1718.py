# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-11 15:18
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasas', '0017_auto_20160904_1655'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ['anno']},
        ),
        migrations.AlterModelOptions(
            name='tasa',
            options={'ordering': ['curso__anno', 'tipo']},
        ),
        migrations.AlterField(
            model_name='curso',
            name='anno',
            field=models.IntegerField(unique=True, validators=[django.core.validators.RegexValidator(regex='^\\d{4}$')], verbose_name='Año'),
        ),
        migrations.AlterField(
            model_name='universidad',
            name='provincia',
            field=models.CharField(choices=[('Alava', 'Álava'), ('Albacete', 'Albacete'), ('Alicante', 'Alicante'), ('Almeria', 'Almería'), ('Asturias', 'Asturias'), ('Avila', 'Ávila'), ('Badajoz', 'Badajoz'), ('Baleares', 'Baleares'), ('Barcelona', 'Barcelona'), ('Burgos', 'Burgos'), ('Caceres', 'Cáceres'), ('Cadiz', 'Cádiz'), ('Cantabria', 'Cantabria'), ('Castellon', 'Castellón'), ('Ceuta', 'Ceuta'), ('Ciudad Real', 'Ciudad Real'), ('Cordoba', 'Córdoba'), ('Cuenca', 'Cuenca'), ('Gerona', 'Gerona'), ('Granada', 'Granada'), ('Guadalajara', 'Guadalajara'), ('Gipuzkoa', 'Gipuzkoa'), ('Huelva', 'Huelva'), ('Huesca', 'Huesca'), ('Jaen', 'Jaén'), ('La Coruna', 'La Coruña'), ('La Rioja', 'La Rioja'), ('Las Palmas', 'Las Palmas'), ('Leon', 'León'), ('Lerida', 'Lérida'), ('Lugo', 'Lugo'), ('Madrid', 'Madrid'), ('Malaga', 'Málaga'), ('Melilla', 'Melilla'), ('Murcia', 'Murcia'), ('Navarra', 'Navarra'), ('Orense', 'Orense'), ('Palencia', 'Palencia'), ('Pontevedra', 'Pontevedra'), ('Salamanca', 'Salamanca'), ('Santa Cruz de Tenerife', 'Santa Cruz de Tenerife'), ('Segovia', 'Segovia'), ('Sevilla', 'Sevilla'), ('Soria', 'Soria'), ('Tarragona', 'Tarragona'), ('Teruel', 'Teruel'), ('Toledo', 'Toledo'), ('Valencia', 'Valencia'), ('Valladolid', 'Valladolid'), ('Bizkaia', 'Bizkaia'), ('Zamora', 'Zamora'), ('Zaragoza', 'Zaragoza')], help_text='Provincia', max_length=50),
        ),
    ]
