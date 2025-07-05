from .models import Categoria

# Importa a classe base ModelForm
from django.forms import ModelForm

# Define o formulário CategoriaForm para criar e editar instâncias de Categoria
class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']
