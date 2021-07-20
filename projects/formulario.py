from django.forms import ModelForm
from projects.models import Projetos

# Criando a classe do formulário
class ProjetosForm(ModelForm):
    class Meta:
        model = Projetos
        fields = ['numero_projeto', 'nome_projeto', 'data_inicio', 'data_fim']


