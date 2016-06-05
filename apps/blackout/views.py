# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from datetime import datetime
from apps.blackout.models import Document
from apps.blackout.models import Blackouts
from apps.blackout.forms import DocumentForm

#Custom Sheets
import signals


def blackout(request):

    if request.method == 'POST':
        selected_bakery = request.POST.get('selected_bakery')
        #return HttpResponseRedirect(reverse(str(selected_bakery.lower())))
        return HttpResponseRedirect(reverse('submittemplate'))
    else:
        return render(request, 'mdlzntw/blackout.html', {
    
})
    
def submittemplate(request):

    #Bakery Submission Information
    bakery_names = ['Richmond','Fairlawn','Salinas', 'Montreal','East York','Atlanta','Naperville','Monterrey','Portland','Scarborough','Chicago']
    bakery_names.sort()
    cal_months = ['January','Feburary','March','April','May','June','July','August','September','October','November','December']
    template_year = [x for x in range(2015,2021)]
    this_year = int(datetime.now().year)
    this_month = (datetime.now()).strftime("%B")


	#Submitting the file
    if request.method == 'POST':
        
        file_form = DocumentForm(request.POST, request.FILES)
        selected_template_year = request.POST.get('selected_template_year')
        selected_bakery_name = request.POST.get('selected_bakery_name')
        template_file = str(request.FILES['docfile'])
        
        if file_form.is_valid():
            #check is ends in .xlsx here
            newdoc = Document(template_file = request.FILES['docfile'],bakery=selected_bakery_name,temp_year=selected_template_year,sub_month=this_month)
            newdoc.save()

            #Call the file find and upload breakout here to move into other database
            #Find a way to sub in month and year from DB
            signals.breakout_excel_upload(template_file, selected_bakery_name,selected_template_year)
          
            # Go here after post
            return HttpResponseRedirect('/blackout/')
    else:
        file_form = DocumentForm() 

    return render(request, 'mdlzntw/submit_template.html', {
    
    'bakery_names': bakery_names,
    'file_form': file_form,
    'template_year': template_year,
    'this_year':this_year,
    'this_month':this_month,
    'cal_months':cal_months
})
    





