# -*- coding: utf-8 -*-
from django.shortcuts import render
 
def home(request):
	import os
	print (os.path.dirname(os.path.abspath(__file__)))

	return render(request, "mdlzntw/index.html", {})