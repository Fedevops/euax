from django.forms import ModelForm
from activities.models import Atividades

# Criando a classe do formulário para cadastro de nova atividade
class AtividadesForm(ModelForm):
    class Meta:
        model = Atividades
        fields = ['id_projeto', 'nome_atividade', 'data_inicio', 'data_fim', 'situacao']


