from projects.models import Projetos
from django.db import models

## Criação de modelos de dados para persistência no banco de dados
class Atividades(models.Model):
    id_projeto = models.ManyToManyField(Projetos, related_name="projetos")
    nome_atividade = models.CharField(max_length=30)
    data_inicio = models.DateField('Data Inicio')
    data_fim = models.DateField('Data Fim')
    situacao = models.BooleanField(default=True)
    
    