from .models import Usuario
from django.forms import ModelForm

# Importando os formulários já prontos do Django para criação e edição de usuários
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# Formulário para criar um novo usuário, utilizando o UserCreationForm do Django
class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'telefone', 'endereco']

# Formulário para editar um usuário existente, utilizando o UserChangeForm do Django
class UsuarioEditForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'telefone', 'endereco']
        