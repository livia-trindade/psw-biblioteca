from django.urls import path
from . import views # Importa as views de emprestimo

# Lista de urls de emprestimo
urlpatterns = [
    path('', views.index, name='index-emprestimo'),
    path('<int:id_emprestimo>/', views.detalha, name='index-detalha'),
    path('create/', views.create, name='create-emprestimo'),
    path('update/<int:id_emprestimo>/', views.update, name='update-emprestimo'),
    path('delete/<int:id_emprestimo>/', views.delete, name='delete-emprestimo')
]