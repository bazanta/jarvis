# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-13 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0003_auto_20171113_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficheproduit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'product'),
        ),
    ]
