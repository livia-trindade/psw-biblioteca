from django.db import models

# Definindo o modelo Autor
class Autor(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)
    

    class Meta:
        # Definindo o nome da tabela no banco de dados
        db_table = "Autor_autores"
        # Criando uma permissão
        permissions = [
            ("detail_autor", "Pode ver o detalhe de autor"),
        ]

# Definindo como o objeto será representado como string 
    def __str__(self):
        return self.nome