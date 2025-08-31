from django.db import models

# Importa o modelo Autor do app autor
from autor.models import Autor

# Importa o modelo Categoria do app categoria
from categoria.models import Categoria


# Define o modelo Livro
class Livro(models.Model):
    nome = models.CharField(max_length=100)

    # Campo ISBN - máximo de 13 caracteres e valor único
    isbn = models.CharField("ISBN", max_length=13, unique=True)

    ano_publicacao = models.PositiveIntegerField(blank=True, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    quantidade = models.PositiveIntegerField("Estoque", default=1)
    editora = models.CharField(max_length=100, blank=True, null=True)


    class Meta:
        # Define o nome da tabela no banco de dados
        db_table = "Livro_livro"

    # Define a representação em string
    def __str__(self):
        return self.nome
