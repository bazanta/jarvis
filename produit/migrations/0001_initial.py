# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-13 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FicheProduit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('reference', models.CharField(max_length=45)),
                ('descCourte', models.CharField(max_length=100)),
                ('descLong', models.CharField(max_length=255)),
                ('enStock', models.BooleanField(default=True)),
            ],
        ),
    ]
