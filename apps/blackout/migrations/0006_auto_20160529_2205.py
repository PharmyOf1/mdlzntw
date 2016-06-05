# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-29 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackout', '0005_remove_document_bakery'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='bakery',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='temp_year',
            field=models.IntegerField(null=True),
        ),
    ]
