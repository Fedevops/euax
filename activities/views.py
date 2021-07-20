"""
Im
"""
# Importação de bibliotecas e componentes
from django.shortcuts import redirect, render
from activities.formulario import AtividadesForm
from activities.models import Atividades
from projects.models import Projetos

"""
Criação de Views pata exibição no front End
Autor: Fernando Silva
Data: 20/07/2021

"""
# função para a view "home"
def homea(request):
    data = {}
    data['dba'] = Atividades.objects.all()
    return render (request, 'homea.html', data)

# função para a view "formulário de nova atividade"
def forma(request):
    data = {}
    data['forma'] = AtividadesForm()
    return render(request, 'forma.html', data)

# função para a criação
def creata(request):
    if request.method == 'POST':
        form = AtividadesForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('homea')
        else:
            return render(request, 'forma.html')
    else:
        return render(
            request, 'forma.html'
        )
        
# função para a visualização
def viewa(request, pk):
    data = {}
    data['dba'] = Atividades.objects.get(pk=pk)
    return render(request, 'viewa.html', data)       
   
# função para a edição
def edita(request, pk):
    data = {}
    data['dba'] = Atividades.objects.get(pk=pk)
    data['forma'] = AtividadesForm(instance=data['dba'])
    return render(request, 'forma.html', data)

# função para a atualização
def updatea(request, pk):
    data = {}
    data['dba'] = Atividades.objects.get(pk=pk)
    form = AtividadesForm(request.POST or None, instance=data['dba'])
    if form.is_valid:
        form.save()
        return redirect('homea') 

# função para a deleção
def deletea(request, pk):
    dba = Atividades.objects.get(pk=pk)
    dba.delete()
    return redirect('homea')
        
            
       