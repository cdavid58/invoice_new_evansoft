from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
# from django.conf.urls import handler404, handler500
# from errors.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('authentication.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^supplier/', include('supplier.urls')),
    url(r'^inventory/', include('inventory.urls')),
    url(r'^shopping/', include('shopping.urls')),
    url(r'^invoice/', include('invoice.urls')),
    url(r'^client/', include('client.urls')),
    url(r'^emails/', include('emails.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# handler404 = handler404
# handler500 = handler500