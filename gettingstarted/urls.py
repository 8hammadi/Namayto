from django.urls import path, include
from django.contrib import admin
from gettingstarted import  settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
admin.autodiscover()

urlpatterns = [
	path('',include('api.urls'))

]
