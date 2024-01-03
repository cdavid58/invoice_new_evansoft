from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Index/$',Index,name="Index"),
	url(r'^Settings/$',Settings,name="Settings"),
]