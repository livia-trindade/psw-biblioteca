# Importa a função render para renderizar templates HTML
from django.shortcuts import render

# Importa classes de resposta HTTP para redirecionamento e respostas simples
from django.http import HttpResponse, HttpResponseRedirect

# Importa o modelo Livro e o formulário LivroForm do app livro
from .models import Livro
from .forms import LivroForm

# Importa decoradores para exigir login e permissões específicas
from django.contrib.auth.decorators import login_required, permission_required


# View que lista todos os livros cadastrados - exibida apenas para usuários logados e com permissão 'view_livro'
@login_required
@permission_required('livro.view_livro', raise_exception=True)
def index(request):
    livros = Livro.objects.all()
    return render(request, 'livro/index.html', {'livros': livros})


# View que mostra os detalhes de um livro específico - exibida apenas para usuários logados e com permissão 'detail_livro'
@login_required
@permission_required('livro.detail_livro', raise_exception=True)
def detalha(request, id_livro):
    livro = Livro.objects.get(id=id_livro)
    return render(request, 'livro/detalha.html', {'livro': livro})


# View para criar um novo livro - exibida apenas para usuários logados e com permissão 'add_livro'
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


# View para editar um livro existente - exibida apenas para usuários logados e com permissão 'change_livro'
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


# View para excluir um livro - exibida apenas para usuários logados e com permissão 'delete_livro'
@login_required
@permission_required('livro.delete_livro', raise_exception=True)
def delete(request, id_livro):
    livro = Livro.objects.get(id=id_livro)
    livro.delete()
    return HttpResponseRedirect("/livro/")


# View de exemplo que exibe uma mensagem fixa - exibida apenas para usuários logados e com permissão 'view_livro'
@login_required
@permission_required('livro.view_livro', raise_exception=True)
def read(request):
    return HttpResponse("<h3>Aqui que lê!</h3>")
