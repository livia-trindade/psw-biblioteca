from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Autor
from .forms import AutorForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('autor.view_autor', raise_exception=True)
def index(request):
    autores = Autor.objects.all()
    return render(request, 'autor/index.html', {'autores': autores})

@login_required
@permission_required('autor.detail_autor', raise_exception=True)
def detalha(request, id_autor):
    autor = Autor.objects.get(id=id_autor)
    return render(request, 'autor/detalha.html', {'autor': autor})

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

@login_required
@permission_required('autor.delete_autor', raise_exception=True)
def delete(request, id_autor):
    autor = Autor.objects.get(id=id_autor)
    autor.delete()
    return HttpResponseRedirect("/autor/")

