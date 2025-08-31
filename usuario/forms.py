from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

# Formulário para criar um novo usuário, utilizando o UserCreationForm do Django
class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        # Inclui username, senhas e seus campos extras
        fields = ['username', 'nome', 'telefone', 'cidade', 'rua', 'bairro', 'numero','password1', 'password2']

# Formulário para editar um usuário existente, utilizando o UserChangeForm do Django
class UsuarioEditForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['username', 'nome', 'telefone','cidade', 'rua', 'bairro', 'numero']
