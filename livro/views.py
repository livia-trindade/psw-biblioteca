from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Livro
from .forms import LivroForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('livro.view_livro', raise_exception=True)
def index(request):
    livroes = Livro.objects.all()
    return render(request, 'livro/index.html', {'livroes': livroes})

@login_required
@permission_required('livro.detail_livro', raise_exception=True)
def detalha(request, id_livro):
    livro = Livro.objects.get(id=id_livro)
    return render(request, 'livro/detalha.html', {'livro': livro})

@login_required
@permission_required('livro.add_livro', raise_exception=True)
def create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/livro/")
    else:
        form = LivroForm()
    return render(request, 'livro/create.html', {'form': form})

@login_required
@permission_required('livro.change_livro', raise_exception=True)
def update(request, id_livro):
    livro = Livro.objects.get(id=id_livro)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/livro/")
    else:
        form = LivroForm(instance=livro)
    return render(request, 'livro/update.html', {'form': form})

@login_required
@permission_required('livro.delete_livro', raise_exception=True)
def delete(request, id_livro):
    livro = Livro.objects.get(id=id_livro)
    livro.delete()
    return HttpResponseRedirect("/livro/")

@login_required
@permission_required('livro.view_livro', raise_exception=True)
def read(request):
    return HttpResponse("<h3>Aqui que lê!</h3>")