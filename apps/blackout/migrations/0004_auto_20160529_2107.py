# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-29 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackout', '0003_auto_20160529_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='bakery',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]