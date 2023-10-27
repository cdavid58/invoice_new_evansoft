from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^List_Supplier/$',List_Supplier,name="List_Supplier"),
	url(r'^Create_Supplier/$',Create_Supplier,name="Create_Supplier"),
	url(r'^Delete_Supplier/$',Delete_Supplier,name="Delete_Supplier"),
	url(r'^Edit_Supplier/(\d+)/$',Edit_Supplier,name="Edit_Supplier"),
]