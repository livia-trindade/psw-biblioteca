from django.db import models

# Define Categoria que será armazenado no banco de dados
class Categoria(models.Model):
    # Campo para o nome da categoria (obrigatório e único)
    nome = models.CharField(max_length=100, unique=True)
    
    # Campo para uma descrição opcional da categoria
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        # Define o nome da tabela no banco de dados
        db_table = "Categorias_categorias"

        # Define permissões personalizadas além das padrão do Django
        permissions = [
            ("detail_categoria", "Pode ver o detalhe de categoria"),
        ]

    # Define a representação em string
    def __str__(self):
        return self.nome
