from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Inbox/$',Inbox,name="Inbox"),
	url(r'^Sender/$',Sender,name="Sender"),
	url(r'^Composer/$',Composer,name="Composer"),
]