from django.conf.urls import patterns, url

from .views import blackout, submittemplate

urlpatterns = patterns('blackout.views',
	url(r'^$', blackout, name="blackout"),
    url(r'^submittemplate', submittemplate, name="submittemplate"),
)