from .models import Emprestimo

# Importa classes base do Django para criar formulários
from django.forms import ModelForm, Select, DateInput

# Define o formulário EmprestimoForm para criar e editar registros de empréstimos
class EmprestimoForm(ModelForm):
    class Meta:
        # Define o modelo usado pelo formulário
        model = Emprestimo

        # Define os campos do modelo que vão aparecer no formulário
        fields = [
            'usuario',
            'livro',
            'data_devolucao'
        ]

        # Define widgets para melhorar a aparência no template
        widgets = {
            'usuario': Select(attrs={'class': 'form-control'}),         # Dropdown para selecionar o usuário
            'livro': Select(attrs={'class': 'form-control'}),           # Dropdown para selecionar o livro
            'data_devolucao': DateInput(attrs={                         # Campo de data com seletor
                'class': 'form-control',
                'type': 'date'  # HTML5 date picker
            }),
        }
