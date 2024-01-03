from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^$',Login,name="Login"),
	url(r'^List_Employee/$',List_Employee,name="List_Employee"),
	url(r'^LogOut/$',LogOut,name="LogOut"),
	url(r'^Create_Employee/$',Create_Employee,name="Create_Employee"),
	url(r'^Get_Employee/(\d+)/$',Get_Employee,name="Get_Employee"),
	url(r'^Update_Data_Employee/$',Update_Data_Employee,name="Update_Data_Employee"),
	url(r'^Delete_Employee/$',Delete_Employee,name="Delete_Employee"),
	url(r'^Query_Permissions/$',Query_Permissions,name="Query_Permissions"),
]