from django.contrib import admin
from django.urls import path, include 

from usuario import views as views_usuario
from autor import views as views_autor
from categoria import views as views_categoria
from livro import views as views_livro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conta/', include('django.contrib.auth.urls')),
    path('usuario/', include('usuario.urls')),
    path('autor/', include('autor.urls')),
    path('categoria/', include('categoria.urls')),
    path('livro/', include('livro.urls')),
    ]