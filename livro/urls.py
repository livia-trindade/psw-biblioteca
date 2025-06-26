from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index-livro'),
    path('<int:id_livro>/', views.detalha, name='index-detalha'),
    path('create/', views.create, name='create-livro'),
    path('update/<int:id_livro>/', views.update, name='update-livro'),
    path('delete/<int:id_livro>/', views.delete, name='delete-livro')
]