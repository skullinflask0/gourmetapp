from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("gourmet/", include('gourmet.urls')),
    path('admin/', admin.site.urls),
]
