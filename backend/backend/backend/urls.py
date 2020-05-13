from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('enhance/', include('enhance.urls')),
    path('admin/', admin.site.urls),
]