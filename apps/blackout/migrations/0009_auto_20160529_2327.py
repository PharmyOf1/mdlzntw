# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-29 23:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blackout', '0008_document_upload_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='docfile',
            new_name='template_file',
        ),
    ]
