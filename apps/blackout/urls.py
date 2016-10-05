from django.conf.urls import url

from .views import blackout, submittemplate
from apps.blackout.views import dltemplate, filedownload, indy_bakery, blackout_new
#from apps.blackout.views import richmond,fairlawn,atlanta,portland,chicago,naperville,salinas,monterrey,eastyork,scarborough,montreal

urlpatterns = [
	url(r'^$', blackout_new, name="blackout"),
	url(r'^dltemplate', dltemplate, name="dltemplate"),
	url(r'^filedownload', filedownload, name="filedownload"),
    url(r'^submittemplate', submittemplate, name="submittemplate"),
    url(r'^richmond', indy_bakery, name="richmond"),
    url(r'^fairlawn', indy_bakery, name="fairlawn"),
    url(r'^atlanta', indy_bakery, name="atlanta"),
    url(r'^portland', indy_bakery, name="portland"),
    url(r'^chicago', indy_bakery, name="chicago"),
    url(r'^naperville', indy_bakery, name="naperville"),
    url(r'^salinas', indy_bakery, name="salinas"),
    url(r'^monterrey', indy_bakery, name="monterrey"),
    url(r'^eastyork', indy_bakery, name="eastyork"),
    url(r'^scarborough', indy_bakery, name="scarborough"),
    url(r'^montreal', indy_bakery, name="montreal")
]
