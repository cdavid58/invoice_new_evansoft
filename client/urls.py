from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Get_List_Customer/$',Get_List_Customer,name="Get_List_Customer"),
	url(r'^Edit_Customer/(\d+)/$',Edit_Customer,name="Edit_Customer"),
	url(r'^Create_Customer/$',Create_Customer,name="Create_Customer"),
]