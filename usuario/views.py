from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Usuario
from .forms import UsuarioForm, UsuarioEditForm
from django.contrib.auth.decorators import login_required, permission_required


@login_required
@permission_required('usuario.view_usuario', raise_exception=True)
def index(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/index.html', {'usuarios': usuarios})

@login_required
@permission_required('usuario.detail_usuario', raise_exception=True)
def detalha(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario) 
    return render(request, 'usuario/detalha.html', {'usuario': usuario})

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

@login_required
@permission_required('usuario.delete_usuario', raise_exception=True)
def delete(request, id_usuario):
    Usuario.objects.get(id=id_usuario).delete()
    return HttpResponseRedirect("/usuario/")