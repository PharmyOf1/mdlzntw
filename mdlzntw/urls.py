from django.conf.urls import url, include
from django.contrib import admin

#Docs
from django.conf import settings
from django.conf.urls.static import static
#

from .views import home, network, test, login_user
from apps.blackout import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^test', test, name='test'),
    url(r'^blackout/', include('apps.blackout.urls')),
    url(r'^login', login_user, name='login_user')
    ]
