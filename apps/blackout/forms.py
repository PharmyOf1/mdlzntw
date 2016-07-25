# -*- coding: utf-8 -*-

from django import forms

class DocumentForm(forms.Form):
	docfile = forms.FileField(label='Select a file')

#ajax testinig

class YourForm(forms.Form):    
    industry = forms.ChoiceField(choices=['sup','foo'])
    sector = forms.ChoiceField(choices=['sip','2'])   