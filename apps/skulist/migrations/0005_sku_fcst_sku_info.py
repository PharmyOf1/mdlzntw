# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-27 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skulist', '0004_auto_20160527_0826'),
    ]

    operations = [
        migrations.CreateModel(
            name='SKU_FCST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, db_column='SKU', max_length=30, null=True)),
                ('calmonth', models.IntegerField(blank=True, db_column='CALMONTH', null=True)),
                ('calyear', models.IntegerField(blank=True, db_column='CALYEAR', null=True)),
                ('cases', models.IntegerField(blank=True, db_column='CASES', null=True)),
                ('pounds', models.FloatField(blank=True, db_column='POUNDS', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SKU_INFO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, db_column='KGF_STD_ITEM_CDE', max_length=14, null=True)),
                ('short_description', models.CharField(blank=True, db_column='SHORT_DESCRIPTION', max_length=40, null=True)),
                ('gross_wt_cse_qty', models.CharField(blank=True, db_column='GROSS_WT_CSE_QTY', max_length=40, null=True)),
                ('cube_adjusted_wt', models.CharField(blank=True, db_column='CUBE_ADJUSTED_WT', max_length=40, null=True)),
                ('case_per_mfg_stack', models.CharField(blank=True, db_column='CASE_PER_MFG_STACK', max_length=40, null=True)),
                ('net_wt_cse_qty', models.CharField(blank=True, db_column='NET_WT_CSE_QTY', max_length=40, null=True)),
                ('std_itm_cd', models.CharField(blank=True, db_column='STD_ITM_CD', max_length=40, null=True)),
                ('capacity_grp_cd', models.CharField(blank=True, db_column='CAPACITY_GRP_CD', max_length=40, null=True)),
            ],
        ),
    ]
