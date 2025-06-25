from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "usuarios_usuarios"
        permissions = [
            ("detail_usuario", "Pode ver o detalhe de usuário"),
        ]

    def __str__(self):
        return self.nome