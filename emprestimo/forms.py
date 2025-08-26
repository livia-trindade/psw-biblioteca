from .models import Emprestimo
from django.forms import ModelForm, Select, DateInput

class EmprestimoForm(ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['usuario', 'livro']  # NÃO incluir data_devolucao aqui
        widgets = {
            'usuario': Select(attrs={'class': 'form-control'}),
            'livro': Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.request:
            instance.administrador = self.request.user
        if commit:
            instance.save()
        return instance
