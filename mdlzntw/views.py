# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

#This is the view called requiring a login

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    #return render_to_response('mdlzntw/login.html', context_instance=RequestContext(request))
    return render(request,'mdlzntw/login.html')


@login_required(login_url='/login')
def home(request):

	return render(request, "mdlzntw/index.html", {})

@login_required(login_url='/login')
def network(request):

	return render(request, "mdlzntw/index.html", {})


def test(request):
	from apps.skulist.models import SKU_INFO
	from apps.skulist.models import SKU_FCST

	er_thing = SKU_INFO.objects.all()
	fcst_all = SKU_FCST.objects.all()
	# print (er_thing)

	test_dict = {
					'er_thing':er_thing,
					'fcst_all':fcst_all


				}
	return render(request, "mdlzntw/test.html", test_dict)
