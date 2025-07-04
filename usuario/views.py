from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Importando o models.py e os formulários (forms.py) do app usuario
from .models import Usuario
from .forms import UsuarioForm, UsuarioEditForm

# Importando os decoradores para exigir login e permissões 
from django.contrib.auth.decorators import login_required, permission_required


# View que lista todos os usuários cadastrados - exibida apenas para usuários logados e com permissão 'view_usuario'
@login_required
@permission_required('usuario.view_usuario', raise_exception=True)
def index(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/index.html', {'usuarios': usuarios})

# View que mostra os detalhes de um usuário específico - exibida apenas para usuários logados e com permissão 'detail_usuario'
@login_required
@permission_required('usuario.detail_usuario', raise_exception=True)
def detalha(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario) 
    return render(request, 'usuario/detalha.html', {'usuario': usuario})

# View para criar um novo usuário - exibida apenas para usuários logados e com permissão 'add_usuario'
@login_required
@permission_required('usuario.add_usuario', raise_exception=True)
def create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/usuario/")    
    else:
        form = UsuarioForm()
    return render(request, 'usuario/create.html', {'form': form})

# View para editar um usuário existente -  exibida apenas para usuários logados e com permissão 'change_usuario'
@login_required
@permission_required('usuario.change_usuario', raise_exception=True)
def update(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    if request.method == 'POST':
        form = UsuarioEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/usuario/")    
    else:
        form = UsuarioEditForm(instance=usuario)
    return render(request, 'usuario/update.html', {'form': form})

# View para excluir um usuário - exibida apenas para usuários logados e com permissão 'delete_usuario'
@login_required
@permission_required('usuario.delete_usuario', raise_exception=True)
def delete(request, id_usuario):
    Usuario.objects.get(id=id_usuario).delete()
    return HttpResponseRedirect("/usuario/")