from django.db import models
from autor.models import Autor
from categoria.models import Categoria


class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        db_table = "Livro_livro"


    def __str__(self):
        return self.nome