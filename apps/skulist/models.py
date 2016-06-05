# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
 
from . import managers
 
 
class Profile(models.Model):
    # Relations
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="profile",
        verbose_name=_("user")
        )
    # Attributes - Mandatory
    interaction = models.PositiveIntegerField(
        default=0,
        verbose_name=_("interaction")
        )
    # Attributes - Optional
    # Object Manager
    objects = managers.ProfileManager()
 
    # Custom Properties
    @property
    def username(self):
        return self.user.username
 
    # Methods
 
    # Meta and String
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        ordering = ("user",)
 
    def __str__(self):
        return self.user.username


class SKU_FCST(models.Model):
    sku = models.CharField(db_column='SKU', max_length=30, blank=True, null=True) 
    calmonth = models.IntegerField(db_column='CALMONTH', blank=True, null=True) 
    calyear = models.IntegerField(db_column='CALYEAR', blank=True, null=True) 
    cases = models.IntegerField(db_column='CASES', blank=True, null=True) 
    pounds = models.FloatField(db_column='POUNDS', blank=True, null=True) 

class SKU_INFO(models.Model):
    item = models.CharField(db_column='KGF_STD_ITEM_CDE', max_length=14, blank=True, primary_key=True)  
    short_description = models.CharField(db_column='SHORT_DESCRIPTION', max_length=40, blank=True, null=True) 
    gross_wt_cse_qty = models.CharField(db_column='GROSS_WT_CSE_QTY', max_length=40, blank=True, null=True)  
    cube_adjusted_wt = models.CharField(db_column='CUBE_ADJUSTED_WT', max_length=40, blank=True, null=True)  
    case_per_mfg_stack = models.CharField(db_column='CASE_PER_MFG_STACK', max_length=40, blank=True, null=True)  
    net_wt_cse_qty = models.CharField(db_column='NET_WT_CSE_QTY', max_length=40, blank=True, null=True)  
    std_itm_cd = models.CharField(db_column='STD_ITM_CD', max_length=40, blank=True, null=True)  
    capacity_grp_cd = models.CharField(db_column='CAPACITY_GRP_CD', max_length=40, blank=True, null=True) 



    
