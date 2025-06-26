from .models import Livro
from django.forms import ModelForm, TextInput, Select, NumberInput

class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'isbn', 'editora', 'ano_publicacao', 'quantidade', 'autor', 'categoria']
        widgets = {
            'nome': TextInput(attrs={'class': 'form-control'}),
            'isbn': TextInput(attrs={'class': 'form-control'}),
            'editora': TextInput(attrs={'class': 'form-control'}),
            'ano_publicacao': NumberInput(attrs={'class': 'form-control'}),
            'quantidade': NumberInput(attrs={'class': 'form-control'}),
            'autor': Select(attrs={'class': 'form-select'}),
            'categoria': Select(attrs={'class': 'form-select'}),
        }
