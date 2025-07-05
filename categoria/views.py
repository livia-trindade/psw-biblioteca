# Importa a função render para renderizar templates HTML
from django.shortcuts import render

# Importa classes de resposta HTTP para redirecionamento
from django.http import HttpResponse, HttpResponseRedirect

# Importa o modelo Categoria e o formulário CategoriaForm do app categoria
from .models import Categoria
from .forms import CategoriaForm

# Importa decoradores para exigir login e permissões específicas
from django.contrib.auth.decorators import login_required, permission_required


# View que lista todas as categorias cadastradas - exibida apenas para usuários logados e com permissão 'view_categoria'
@login_required
@permission_required('categoria.view_categoria', raise_exception=True)
def index(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria/index.html', {'categorias': categorias})


# View que mostra os detalhes de uma categoria específica - exibida apenas para usuários logados e com permissão 'detail_categoria'
@login_required
@permission_required('categoria.detail_categoria', raise_exception=True)
def detalha(request, id_categoria):
    categoria = Categoria.objects.get(id=id_categoria)
    return render(request, 'categoria/detalha.html', {'categoria': categoria})


# View para criar uma nova categoria - exibida apenas para usuários logados e com permissão 'add_categoria'
@login_required
@permission_required('categoria.add_categoria', raise_exception=True)
def create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/categoria/")
    else:
        form = CategoriaForm()
    return render(request, 'categoria/create.html', {'form': form})


# View para editar uma categoria existente - exibida apenas para usuários logados e com permissão 'change_categoria'
@login_required
@permission_required('categoria.change_categoria', raise_exception=True)
def update(request, id_categoria):
    categoria = Categoria.objects.get(id=id_categoria)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/categoria/")
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categoria/update.html', {'form': form})


# View para excluir uma categoria - exibida apenas para usuários logados e com permissão 'delete_categoria'
@login_required
@permission_required('categoria.delete_categoria', raise_exception=True)
def delete(request, id_categoria):
    categoria = Categoria.objects.get(id=id_categoria)
    categoria.delete()
    return HttpResponseRedirect("/categoria/")
