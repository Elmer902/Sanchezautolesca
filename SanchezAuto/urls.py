from django.contrib import admin
from baton.autodiscover import admin
from django.urls import path,include

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    path('', include('base.urls')),
]
