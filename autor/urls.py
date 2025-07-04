from django.urls import path
from . import views # Importando as views do app Autor

# Lista de URLS do app Autor
urlpatterns = [
    path('', views.index, name='index-autor'),
    path('<int:id_autor>/', views.detalha, name='index-detalha'),
    path('create/', views.create, name='create-autor'),
    path('update/<int:id_autor>', views.update, name='update-autor'),
    path('delete/<int:id_autor>', views.delete, name='delete-autor')
]