from django.db import models
from usuario.models import Usuario
from livro.models import Livro
from django.utils import timezone
from datetime import timedelta

class Emprestimo(models.Model):
    STATUS_CHOICES = (
        ('andamento', 'Em andamento'),
        ('atrasado', 'Atrasado'),
        ('devolvido', 'Devolvido'),
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        related_name='emprestimos_recebidos'
    )
    administrador = models.ForeignKey(
        Usuario,
        on_delete=models.SET_NULL,
        null=True,
        related_name='emprestimos_feitos'
    )
    livro = models.ForeignKey(Livro, on_delete=models.SET_NULL, null=True)
    
    data_emprestimo = models.DateField(default=timezone.now) #
    data_prevista_devolucao = models.DateField(blank=True, null=True) #
    data_devolucao = models.DateField(null=True, blank=True) #
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='andamento')

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        # Garante que data_emprestimo seja um date
        if not self.data_emprestimo:
            self.data_emprestimo = timezone.now().date()
        elif isinstance(self.data_emprestimo, timezone.datetime):
            self.data_emprestimo = self.data_emprestimo.date()

        # Define data_prevista_devolucao apenas se não estiver definida
        if is_new and not self.data_prevista_devolucao:
            self.data_prevista_devolucao = self.data_emprestimo + timedelta(days=7)
        elif isinstance(self.data_prevista_devolucao, timezone.datetime):
            self.data_prevista_devolucao = self.data_prevista_devolucao.date()

        # Atualiza status automaticamente
        hoje = timezone.now().date()
        if self.data_devolucao:
            self.status = 'devolvido'
        elif self.data_prevista_devolucao and self.data_prevista_devolucao < hoje:
            self.status = 'atrasado'
        else:
            self.status = 'andamento'

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.livro} emprestado para {self.usuario} ({self.status})'
