# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
 
from . import managers
import datetime

class Blackouts(models.Model):
    bakery = models.CharField(db_column='BAKERY', max_length=40, blank=True, null=True)
    line_name = models.CharField(db_column='LINE_NAME', max_length=40, blank=True, null=True)
    prod_type = models.CharField(db_column="PROD_TYPE",max_length=40,blank=True,null=True)
    ibl = models.IntegerField(db_column='IBL', blank=True, null=True)
    template_year = models.IntegerField(db_column='TEMPLATE_YEAR', blank=True, null=True)
    submission_month = models.IntegerField(db_column='SUBMISSION_MONTH', blank=True, null=True)
    submission_year = models.IntegerField(db_column='SUBMISSION_YEAR', blank=True, null=True)
    line_number = models.IntegerField(db_column='LINE_NUMBER',  blank=True, null=True)
    jan_straight = models.IntegerField(db_column='JAN_STRAIGHT',  blank=True, null=True)
    jan_ot = models.IntegerField(db_column='JAN_OT',  blank=True, null=True)
    feb_straight = models.IntegerField(db_column='FEB_STRAIGHT',  blank=True, null=True)
    feb_ot = models.IntegerField(db_column='FEB_OT', blank=True, null=True)
    mar_straight = models.IntegerField(db_column='MAR_STRAIGHT', blank=True, null=True)
    mar_ot = models.IntegerField(db_column='MAR_OT', blank=True, null=True)
    apr_straight = models.IntegerField(db_column='APR_STRAIGHT', blank=True, null=True)
    apr_ot = models.IntegerField(db_column='APR_OT',  blank=True, null=True)
    may_straight = models.IntegerField(db_column='MAY_STRAIGHT', blank=True, null=True)
    may_ot = models.IntegerField(db_column='MAY_OT', blank=True, null=True)
    jun_straight = models.IntegerField(db_column='JUN_STRAIGHT', blank=True, null=True)
    jun_ot = models.IntegerField(db_column='JUNE_OT', blank=True, null=True)
    jul_straight = models.IntegerField(db_column='JUL_STRAIGHT', blank=True, null=True)
    jul_ot = models.IntegerField(db_column='JUL_OT', blank=True, null=True)
    aug_straight = models.IntegerField(db_column='AUG_STRAIGHT', blank=True, null=True)
    aug_ot = models.IntegerField(db_column='AUG_OT', blank=True, null=True)
    sep_straight = models.IntegerField(db_column='SEP_STRAIGHT', blank=True, null=True)
    sep_ot = models.IntegerField(db_column='SEP_OT', blank=True, null=True)
    oct_straight = models.IntegerField(db_column='OCT_STRAIGHT', blank=True, null=True)
    oct_ot = models.IntegerField(db_column='OCT_OT', blank=True, null=True)
    nov_straight = models.IntegerField(db_column='NOV_STRAIGHT', blank=True, null=True)
    nov_ot = models.IntegerField(db_column='NOV_OT',  blank=True, null=True)
    dec_straight = models.IntegerField(db_column='DEC_STRAIGHT', blank=True, null=True)
    dec_ot = models.IntegerField(db_column='DEC_OT', blank=True, null=True)

class Document(models.Model):
	template_file = models.FileField(upload_to='')
	bakery = models.CharField(max_length=30,null=True)
	temp_year = models.IntegerField(null=True)
	sub_month = models.CharField(max_length=30,null=True)
	upload_date = models.DateField(_("Date"), default=datetime.date.today)
