from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Get_List_Invoice/(\d+)/$',Get_List_Invoice,name="Get_List_Invoice"),
	url(r'^Annulled_Invoice/$',Annulled_Invoice,name="Annulled_Invoice"),
	url(r'^View_Invoice/(\d+)/$',View_Invoice,name="View_Invoice"),
	url(r'^Print_Invoice/(\d+)/$',Print_Invoice,name="Print_Invoice"),
	url(r'^Create_Invoice/$',Create_Invoice,name="Create_Invoice"),
	url(r'^Loading_Product/$',Loading_Product,name="Loading_Product"),
	url(r'^Save_Invoice/$',Save_Invoice,name="Save_Invoice"),
	url(r'^Get_Number/$',Get_Number,name="Get_Number"),
	url(r'^Return_Products/$',Return_Products,name="Return_Products"),
	url(r'^Return_Product/$',Return_Product,name="Return_Product"),
]