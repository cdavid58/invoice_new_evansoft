from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Get_List_Products/$',Get_List_Products,name="Get_List_Products"),
	url(r'^Create_Product/$',Create_Product,name="Create_Product"),
	url(r'^Get_Subcategory/$',Get_Subcategory,name="Get_Subcategory"),
	url(r'^Load_Inventory_Excel/$',Load_Inventory_Excel,name="Load_Inventory_Excel"),
	url(r'^Delete_Product/$',Delete_Product,name="Delete_Product"),
	url(r'^Edit_Product/(\w+)/$',Edit_Product,name="Edit_Product"),
]