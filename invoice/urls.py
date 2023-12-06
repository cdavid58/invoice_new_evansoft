from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Get_List_Invoice/(\d+)/$',Get_List_Invoice,name="Get_List_Invoice"),
	url(r'^Annulled_Invoice/$',Annulled_Invoice,name="Annulled_Invoice"),
	url(r'^View_Invoice/(\d+)/$',View_Invoice,name="View_Invoice"),
	url(r'^Create_Invoice/$',Create_Invoice,name="Create_Invoice"),
]