from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Register_Purchase/$',Register_Purchase,name="Register_Purchase"),
	url(r'^Get_List_Products_Supplier/$',Get_List_Products_Supplier,name="Get_List_Products_Supplier"),
	url(r'^Verified_Invoice/$',Verified_Invoice,name="Verified_Invoice"),
	url(r'^Save_Shopping/$',Save_Shopping,name="Save_Shopping"),
]