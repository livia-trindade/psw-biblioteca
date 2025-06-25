from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "Categorias_categorias"
        permissions = [
            ("detail_categoria", "Pode ver o detalhe de categoria"),
        ]

    def __str__(self):
        return self.nome