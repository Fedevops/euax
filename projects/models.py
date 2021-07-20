from django.db import models

## Criação de modelos de dados para persistência
class Projetos(models.Model):
    numero_projeto = models.BigAutoField(primary_key=True)
    nome_projeto = models.CharField(max_length=30)
    data_inicio = models.DateField('Data Inicio')
    data_fim = models.DateField('Data Fim')
    
    