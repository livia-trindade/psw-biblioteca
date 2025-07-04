from django.urls import path
from . import views # Importando as views do app Usuario

# Lista de URLS do app Usuario
urlpatterns = [
    path('', views.index, name='index-usuario'),
    path('<int:id_usuario>/', views.detalha, name='index-detalha'),
    path('create/', views.create, name='create-usuario'),
    path('update/<int:id_usuario>', views.update, name='update-usuario'),
    path('delete/<int:id_usuario>', views.delete, name='delete-usuario')
]