from django.db import models
from autor.models import Autor
from categoria.models import Categoria


class Livro(models.Model):
    nome = models.CharField(max_length=100)
    isbn = models.CharField("ISBN", max_length=13, unique=True)
    editora = models.CharField(max_length=100, blank=True, null=True)
    ano_publicacao = models.PositiveIntegerField(blank=True, null=True)
    quantidade = models.PositiveIntegerField("Estoque", default=1)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = "Livro_livro"


    def __str__(self):
        return self.nome