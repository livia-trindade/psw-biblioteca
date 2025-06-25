from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)
    

    class Meta:
        db_table = "Autor_autores"
        permissions = [
            ("detail_autor", "Pode ver o detalhe de autor"),
        ]

    def __str__(self):
        return self.nome