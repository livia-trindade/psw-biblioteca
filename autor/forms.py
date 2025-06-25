from .models import Autor
from django.forms import ModelForm

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'origem']
        