from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("apit/", include("markers.api_urls")),
    path("markers/", include("markers.urls")),
]
