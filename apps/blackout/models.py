# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
 
from . import managers
from datetime import datetime

class Blackouts(models.Model):
    bakery = models.CharField(db_column='BAKERY', max_length=40, blank=True, null=True)
    line_name = models.CharField(db_column='LINE_NAME', max_length=40, blank=True, null=True)
    template_year = models.IntegerField(db_column='TEMPLATE_YEAR', blank=True, null=True)
    submission_year = models.IntegerField(db_column='SUBMISSION_YEAR', blank=True, null=True)
    submission_month = models.IntegerField(db_column='SUBMISSION_MONTH', blank=True, null=True)
    week_date = models.CharField(db_column='WEEK_DATE', max_length=40, blank=True, null=True)
    label = models.CharField(db_column='LABEL', max_length=40, blank=True, null=True)
    shifts = models.CharField(db_column='SHIFTS', max_length=40, blank=True, null=True)
    template_file = models.CharField(db_column='TEMPLATE_FILE', max_length=40, blank=True, null=True)
    uploader = models.CharField(db_column='UPLOADER', max_length=40, blank=True, null=True)
    upload_date = models.DateField(_("Date"), default=datetime.now)



class Document(models.Model):
	template_file = models.FileField(upload_to='')
	bakery = models.CharField(max_length=30,null=True)
	temp_year = models.IntegerField(null=True)
	sub_month = models.CharField(max_length=30,null=True)
	upload_date = models.DateField(_("Date"), default=datetime.now)


class UserProfile(models.Model):

    SELECT_INDUSTRY = 0
    ACCOUNTING = 1
    ADMINISTRATION_OFFICE_SUPPORT = 2
    BANKING_FINANCIAL_SERVICES = 3
    CALL_CENTRE_CUSTOMER_SERVICE = 4
    COMMUNITY_SERVICES_DEVELOPMENT = 5
    CONSTRUCTION = 6
    CONSULTING_STRATEGY = 7
    DESIGN_ARCHITECTURE = 8
    EDUCATION_TRAINING = 9
    ENGINEERING = 10
    EXECUTIVE_GENERAL_MANAGEMENT = 11
    FARMING_ANIMALS_CONSERVATION = 12
    GOVERNMENT_DEFENCE = 13
    GRADUATE_ENTRY_LEVEL = 14
    HEALTHCARE_MEDICAL = 15
    HOSPITALITY_TRAVEL_TOURISM = 16
    HUMAN_RESOURCES_RECRUITMENT = 17
    INSURANCE_SUPERANNUATION = 18
    INFORMATION_TECHNOLOGY_TELECOMMUNICATIONS = 19
    LEGAL = 20
    MANUFACTURING = 21
    MARKETING_COMMUNICATIONS = 22
    MEDIA_ADVERTISING_ARTS_ENTERTAINMENT = 23
    MINING_RESOURCES_ENERGY = 24
    REAL_ESTATE_PROPERTY = 25
    RETAIL_CONSUMER_PRODUCTS = 26
    SALES = 27
    SCIENCE_TECHNOLOGY = 28
    SELF_EMPLOYMENT = 29
    SPORT_RECREATION = 30
    TRADES_SERVICES = 31
    TRANSPORT_LOGISTICS = 32