# Importa a função render para renderizar templates HTML
from django.shortcuts import render

# Importa classes de resposta HTTP para redirecionamento e respostas simples
from django.http import HttpResponse, HttpResponseRedirect

# Importa o modelo Emprestimo e o formulário EmprestimoForm do app emprestimo
from .models import Emprestimo
from .forms import EmprestimoForm

# Importa decoradores para exigir login e permissões específicas
from django.contrib.auth.decorators import login_required, permission_required


# View que lista todos os empréstimos cadastrados - exibida apenas para usuários logados e com permissão 'view_emprestimo'
@login_required
@permission_required('emprestimo.view_emprestimo', raise_exception=True)
def index(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'emprestimo/index.html', {'emprestimos': emprestimos})


# View que mostra os detalhes de um empréstimo específico - exibida apenas para usuários logados e com permissão 'detail_emprestimo'
@login_required
@permission_required('emprestimo.detail_emprestimo', raise_exception=True)
def detalha(request, id_emprestimo):
    emprestimo = Emprestimo.objects.get(id=id_emprestimo)
    return render(request, 'emprestimo/detalha.html', {'emprestimo': emprestimo})


# View para criar um novo empréstimo - exibida apenas para usuários logados e com permissão 'add_emprestimo'
@login_required
@permission_required('emprestimo.add_emprestimo', raise_exception=True)
def create(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/emprestimo/")
    else:
        form = EmprestimoForm()
    return render(request, 'emprestimo/create.html', {'form': form})


# View para editar um empréstimo existente - exibida apenas para usuários logados e com permissão 'change_emprestimo'
@login_required
@permission_required('emprestimo.change_emprestimo', raise_exception=True)
def update(request, id_emprestimo):
    emprestimo = Emprestimo.objects.get(id=id_emprestimo)
    if request.method == 'POST':
        form = EmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/emprestimo/")
    else:
        form = EmprestimoForm(instance=emprestimo)
    return render(request, 'emprestimo/update.html', {'form': form})


# View para excluir um empréstimo - exibida apenas para usuários logados e com permissão 'delete_emprestimo'
@login_required
@permission_required('emprestimo.delete_emprestimo', raise_exception=True)
def delete(request, id_emprestimo):
    emprestimo = Emprestimo.objects.get(id=id_emprestimo)
    emprestimo.delete()
    return HttpResponseRedirect("/emprestimo/")


# View de exemplo que exibe uma mensagem fixa - exibida apenas para usuários logados e com permissão 'view_emprestimo'
@login_required
@permission_required('emprestimo.view_emprestimo', raise_exception=True)
def read(request):
    return HttpResponse("<h3>Aqui que lê empréstimos!</h3>")
