from django.db import models
from usuario.models import Usuario
from livro.models import Livro

class Emprestimo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    livro = models.ForeignKey(Livro, on_delete=models.SET_NULL, null=True)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.livro} emprestado para {self.usuario} em {self.data_emprestimo}'
