from django.contrib import admin
from django.urls import path, include 

from usuario import views as views_usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conta/', include('django.contrib.auth.urls')),
    path('usuario/', include('usuario.urls')),
    ]