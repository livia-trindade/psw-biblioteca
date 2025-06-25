from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index-autor'),
    path('<int:id_autor>/', views.detalha, name='index-detalha'),
    path('create/', views.create, name='create-autor'),
    path('update/<int:id_autor>', views.update, name='update-autor'),
    path('delete/<int:id_autor>', views.delete, name='delete-autor')
]