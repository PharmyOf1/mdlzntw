"""mdlzntw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,patterns,include
from django.contrib import admin

#Docs
from django.conf import settings
from django.conf.urls.static import static
#

from .views import home, network, schedule, bisccfr, blackout, demand, ac, bakeries

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^network', network, name='network'),
    url(r'^schedule', schedule, name='schedule'),
    url(r'^bisccfr', bisccfr, name='bisccfr'),
    url(r'^blackout', blackout, name='blackout'),
    url(r'^demand', demand, name='demand'),
    url(r'^ac', ac, name='ac'),
    url(r'^bakeries', bakeries, name='bakeries'),
]

