# Importando o models Autor e a classe ModelForm para criar formulários baseados no models.py
from .models import Autor
from django.forms import ModelForm

# Formulário para criar um novo autor baseado no models Autor
class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'nacionalidade']
        