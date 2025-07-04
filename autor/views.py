from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Importando o models.py e os formulários (forms.py) do app Autor
from .models import Autor
from .forms import AutorForm

# Importando os decoradores para exigir login e permissões 
from django.contrib.auth.decorators import login_required, permission_required

# View que lista todos os autores cadastrados - exibida apenas para usuários logados 
@login_required
def index(request):
    autores = Autor.objects.all()
    return render(request, 'autor/index.html', {'autores': autores})

# View que mostra os detalhes de um autor específico - exibida apenas para usuários logados 
@login_required
def detalha(request, id_autor):
    autor = Autor.objects.get(id=id_autor)
    return render(request, 'autor/detalha.html', {'autor': autor})

# View para criar um novo autor - exibida apenas para usuários logados e com permissão 'add_autor'
@login_required
@permission_required('autor.add_autor', raise_exception=True)
def create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/autor/")
    else:
        form = AutorForm()
    return render(request, 'autor/create.html', {'form': form})

# View para editar um autor existente -  exibida apenas para usuários logados e com permissão 'change_autor'
@login_required
@permission_required('autor.change_autor', raise_exception=True)
def update(request, id_autor):
    autor = Autor.objects.get(id=id_autor)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/autor/")
    else:
        form = AutorForm(instance=autor)
    return render(request, 'autor/update.html', {'form': form})

# View para excluir um autor - exibida apenas para usuários logados e com permissão 'delete_autor'
@login_required
@permission_required('autor.delete_autor', raise_exception=True)
def delete(request, id_autor):
    autor = Autor.objects.get(id=id_autor)
    autor.delete()
    return HttpResponseRedirect("/autor/")

