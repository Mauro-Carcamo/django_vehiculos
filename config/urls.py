
from django.contrib import admin
from django.urls import path, include
from vehiculo import views,urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('vehiculo.urls')),
    path("accounts/", include("django.contrib.auth.urls"))
]
