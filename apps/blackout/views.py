# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db import connection
from django.contrib.auth.decorators import login_required

from apps.blackout.models import Document
from apps.blackout.models import Blackouts
from apps.blackout.forms import DocumentForm

#Custom Sheets
import signals
from datetime import datetime, date
import pandas as pd
import numpy as np
import os


def blackout(request):

    #Get unique items with sets
    u_bakeries = Blackouts.objects.order_by().values_list('bakery',flat=True).distinct()
    u_weeks = Blackouts.objects.order_by().values_list('week_date',flat=True).distinct()
    u_lines = sorted(Blackouts.objects.order_by().values_list('line_name',flat=True).distinct())
    u_months = ['Month 01','Month 02','Month 03','Month 04','Month 05','Month 06','Month 07','Month 08','Month 09','Month 10','Month 11','Month 12']
    u_years = list([x for x in range(2015,2020)])

    t_tags = {

                 'u_bakeries': u_bakeries,
                 'u_weeks': u_weeks,
                 'u_years': u_years,
                 'u_months': u_months,
                 'u_lines': u_lines
            }


    bakery_filter = request.POST.getlist('bakery_filter')
    line_filter = request.POST.getlist('line_filter')
    week_filter = request.POST.getlist('week_filter')
    year_filter = request.POST.getlist('year_filter')
    month_filter = request.POST.getlist('month_filter')


    #Error check if nothing selected
    if len(bakery_filter)==0:
        bakery_filter = u_bakeries
    if len(line_filter)==0:
        line_filter = u_lines
    if len(week_filter)==0:
        week_filter = u_weeks
    if len(year_filter)==0:
        year_filter = u_years
    if len(month_filter)==0:
        month_filter = u_months


    if request.method == 'POST':
        t_tags['on_load'] = signals.call_raw_on_load(bakery_filter,line_filter,year_filter,week_filter)
        t_tags['selector'] = 0
        t_tags['fin_months'] = month_filter

        return render(request, 'mdlzntw/blackout.html', t_tags)
    else:   
        
        #t_tags['on_load'] = signals.call_raw_on_load('weeks',bakery_filter,line_filter,year_filter,week_filter)
        #t_tags['selector'] = (len(t_tags['on_load'][0]))

        return render(request, 'mdlzntw/blackout.html', t_tags)


    
def submittemplate(request):

    #Bakery Submission Information
    bakery_names = ['Richmond','Fairlawn','Salinas', 'Montreal','East York','Atlanta','Naperville','Monterrey','Portland','Scarborough','Chicago']
    bakery_names.sort()
    cal_months = ['January','Feburary','March','April','May','June','July','August','September','October','November','December']
    template_year = [x for x in range(2015,2019)]
    this_year = int(datetime.now().year)
    this_month = (datetime.now()).strftime("%B")

    acceptable = ('.xlsx','.xls','.xlsm')

  #Submitting the file
    if request.method == 'POST':
        
        file_form = DocumentForm(request.POST, request.FILES)
        selected_template_year = request.POST.get('selected_template_year')
        selected_bakery_name = request.POST.get('selected_bakery_name')
        template_file = str(request.FILES['docfile'])
        #month nedds to be an integer
        selected_sub_month = int(datetime.strftime(datetime.strptime(request.POST.get('selected_sub_month'),'%B'),'%m'))
        
        if file_form.is_valid() and template_file.endswith(acceptable):
            #check is ends in .xlsx here
            newdoc = Document(template_file = request.FILES['docfile'],bakery=selected_bakery_name,temp_year=selected_template_year,sub_month=this_month)
            newdoc.save()

            last_upload = [a for a in list(Document.objects.all().values_list('template_file'))[-1]][0]


            bo_upload_data = signals.breakout_excel_upload(template_file, selected_bakery_name,selected_template_year,selected_sub_month)
            bulk = [Blackouts(bakery=(t[0]),line_name=t[1],template_year=t[2], submission_year=t[3],submission_month=t[4],week_date=t[5],label=t[6],shifts=t[7],template_file=last_upload,uploader=request.user.username) for t in bo_upload_data]
            Blackouts.objects.bulk_create(bulk)

            print ('Blackout data inserted.')
          
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
    


@login_required(login_url='/login')
def dltemplate(request):
    docs = Document.objects.all().order_by('bakery','-upload_date')
    t_tags = {'docs':docs}

    if request.method == 'POST':
        return render(request, 'mdlzntw/dltemplate.html',t_tags)
    return render(request, 'mdlzntw/dltemplate.html',t_tags)


def filedownload(request):
    if request.method == 'POST':
        template_file = request.POST.get('template_file')
        file_row = Document.objects.get(template_file=template_file)
        template_file = template_file[1:]
        media_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        fsock = open(os.path.join(media_path,'mdlzntw/media{}'.format(template_file)), 'rb')
        response = HttpResponse(fsock, content_type='application/excel')
        response['Content-Disposition'] = "attachment; filename={}".format(file_row.template_file)
        return response
    else:
        return render(request, 'mdlzntw/blackout/dltemplate.html')



@login_required(login_url='/login')
def blackout_new(request):
    t_tags = {}
    return render(request, 'mdlzntw/blackoutmapmain.html',t_tags)



@login_required(login_url='/login')
def indy_bakery(request):
    docs = Document.objects.all().order_by('bakery','-upload_date')

    bakery_name = ''.join([x for x in (str(request).split('/')[-1]) if x.isalpha()])
    
    bake_dict = {
                    'eastyork': 'East York',
                }

    #conversion for text on screen
    if bakery_name in bake_dict.keys():
        bakery_name = bake_dict[bakery_name]
    else: bakery_name = bakery_name.title()

    t_tags = {'bakery':bakery_name,
              'docs':docs}
    return render(request, 'mdlzntw/bakery_blackout_page.html',t_tags)
