import os
import pandas as pd
import openpyxl
import numpy as np
import itertools
import datetime

#Custom Sheets
import sqlcalls

dates_2016 = [x.strftime('%Y-%m-%d') for x in [datetime.date(2015,12,27) + datetime.timedelta(days=x) for x in range(0,364,7)]]
dates_2017 = [x.strftime('%Y-%m-%d') for x in [datetime.date(2016,12,25) + datetime.timedelta(days=x) for x in range(0,364,7)]]
dates_2018 = [x.strftime('%Y-%m-%d') for x in [datetime.date(2017,12,24) + datetime.timedelta(days=x) for x in range(0,364,7)]]

class Blackout_Template():

  def __init__(self, file_name, bakery_name, template_year,sub_month):
    self.file_name = file_name.replace(' ','_')
    self.bakery_name = bakery_name
    self.template_year = template_year

    #Use datetime to log submission month and year - today's date
    self.sub_month = sub_month
    self.sub_year = int(datetime.datetime.now().year)

    self.labels = ['holiday_s','holiday_o','no_ot_s','no_ot_o','shutdown_s','shutdown_o','cleaning_s','cleaning_o', 'maintenance_s','mainteance_o','capital_project_s','capital_project_o','trials_s',
    'trials_o','changeover_s','changeover_o','other_s','other_o']

  def open_file(self):
    #Update to server path and use request.POST for file_name
    path_to_file = (os.path.join((os.path.dirname(os.path.realpath(__file__))),'mdlzntw/media/'))
    
    #load file into memory and convert nums to integers
    check_names = openpyxl.load_workbook(path_to_file + self.file_name).get_sheet_names()

    if 'Original Template' in check_names:
      main_sheet = 'Original Template'
    elif 'Blackout' in check_names:
      main_sheet = 'Blackout'
    else:
      #Salinas/Monterrey
      main_sheet = check_names[0]

    
    blackout = pd.read_excel(path_to_file + self.file_name,sheetname=main_sheet,header=None)
    blackout.fillna(0,inplace=True)
    blackout.apply(pd.to_numeric, errors='ignore')

    return (blackout)
  
  def prepare_for_upload(self,blackout):
    
    #Lines Names from Column 1
    if self.bakery_name=='Montreal':
      names = ['Line 1','Line 2','Line 3', 'Line 5', 'DOYNE', 'Montreal 7B', 'Montreal 8', 'Montreal 00']
    else:
      names = [str(cell) for cell in blackout[0] if '_' in str(cell)]

    #weird way to get list of row numbers where line names are
    list_of_breaks = [list(row_num) for row_num in (np.where(blackout[0].isin(names)))][0]

    #add last rows for last line
    list_of_breaks.append(list_of_breaks[-1]+26)

    #Totals used columns in template
    total_cols = (len(blackout.columns[:]))

    #Tangled web to create a list of slices associated with each line rows
    index_ranges = [slice(list_of_breaks[a:a+2][0],list_of_breaks[a:a+2][1]-9) for a,b in enumerate(list_of_breaks) if len(list_of_breaks[a:a+2])==2]

    #Create dictionary | line:slice
    lines_and_ranges = dict(zip(names,index_ranges))

    #Set week upload based on template date
    if int(self.template_year) == 2016:
        weeks = [x.strftime('%Y-%m-%d') for x in [datetime.date(2015,12,27) + datetime.timedelta(days=x) for x in range(0,364,7)]]
    elif int(self.template_year) == 2017:
        weeks = [x.strftime('%Y-%m-%d') for x in [datetime.date(2016,12,25) + datetime.timedelta(days=x) for x in range(0,364,7)]]
    else:
        weeks = [x.strftime('%Y-%m-%d') for x in [datetime.date(2017,12,24) + datetime.timedelta(days=x) for x in range(0,364,7)]]

    big_guy = []

    #Begin looping through dict to pull out each line range from dataframe, note it's a random line, not in order due to dict
    for line, rng in lines_and_ranges.items():
      line_shifts_only = (blackout.ix[rng,4:total_cols])
      active_line = list(map(list,line_shifts_only.values))

      #Add standards to active line
      for label, a in enumerate(active_line):
        [a.insert(0,x) for x in [self.labels[label],self.sub_month,self.sub_year,self.template_year,line,self.bakery_name]]
        standard, flip = a[:5],a[5:]
  
        #Combine standards with label and input couples onto the active line list
        wrangle = [[flip[0],a] for a in flip if str(a) not in flip[0]]

        #Add week numbers across to match up with shift  
        for num, grouping in enumerate(wrangle):
          grouping.insert(0,weeks[num])

          #Itertools to flatten lists of list(standards) + list(coupled label and shift and date)
          final = tuple(itertools.chain.from_iterable([standard,grouping]))
          big_guy.append(final)

    return big_guy

def breakout_excel_upload(file_name, bakery_name, template_year,sub_month):
  
  BO = Blackout_Template(file_name, bakery_name, template_year,sub_month)
  opened_sheet = BO.open_file()

  return BO.prepare_for_upload(opened_sheet)


def call_raw_on_load(bakery_filter,line_filter,year_filter, week_filter):
	#Raw Sql on initial load
	from django.db import connection, transaction
	cursor = connection.cursor()
	
	bakery_filter = (','.join((['"' + x + '"' for x in bakery_filter])))
	line_filter = (','.join((['"' + x + '"' for x in line_filter])))
	year_filter = (','.join((['"' + str(x) + '"' for x in year_filter])))
	week_filter = (','.join((['"' + x + '"' for x in week_filter])))

	cursor.execute(sqlcalls.main_blackout_call(bakery_filter,line_filter,year_filter,week_filter))

	row = cursor.fetchall()
	return (row)

