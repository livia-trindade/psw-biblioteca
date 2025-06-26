from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index-categoria'),
    path('<int:id_categoria>/', views.detalha, name='index-detalha'),
    path('create/', views.create, name='create-categoria'),
    path('update/<int:id_categoria>', views.update, name='update-categoria'),
    path('delete/<int:id_categoria>', views.delete, name='delete-categoria')
]