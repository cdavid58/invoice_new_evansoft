from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Get_List_Invoice/(\d+)/$',Get_List_Invoice,name="Get_List_Invoice"),
	url(r'^Annulled_Invoice/$',Annulled_Invoice,name="Annulled_Invoice"),
]