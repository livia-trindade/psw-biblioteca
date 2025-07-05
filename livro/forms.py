from .models import Livro

# Importa classes base do Django para criar formulários
from django.forms import ModelForm, TextInput, Select, NumberInput


# Define o formulário LivroForm para criar e editar livros
class LivroForm(ModelForm):
    class Meta:
        # Define o modelo usado pelo formulário
        model = Livro

        # Define os campos do modelo que vão aparecer no formulário
        fields = [
            'nome',
            'isbn',
            'editora',
            'ano_publicacao',
            'quantidade',
            'autor',
            'categoria',
        ]

        # Define widgets para melhorar a aparência no template
        widgets = {
            'nome': TextInput(attrs={'class': 'form-control'}),
            'isbn': TextInput(attrs={'class': 'form-control'}),
            'editora': TextInput(attrs={'class': 'form-control'}),
            'ano_publicacao': NumberInput(attrs={'class': 'form-control'}),
            'quantidade': NumberInput(attrs={'class': 'form-control'}),
            'autor': Select(attrs={'class': 'form-select'}),
            'categoria': Select(attrs={'class': 'form-select'}),
        }
