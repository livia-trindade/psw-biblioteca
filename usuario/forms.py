from .models import Usuario
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'telefone', 'endereco']

class UsuarioEditForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'telefone', 'endereco']
        