# Importação de bibliotecas e componentes
from django.shortcuts import redirect, render
from projects.formulario import ProjetosForm
from projects.models import Projetos



"""
Criação de Views pata exibição no front End
Autor: Fernando Silva
Data: 20/07/2021

"""
# função para a view "home"
def home(request):
    data = {}
    data['db'] = Projetos.objects.all()
    return render (request, 'index.html', data)


# função para a view "formulário de novo Ptojeto"
def form(request):
    data = {}
    data['form'] = ProjetosForm()
    return render(request, 'form.html', data)

# função para a criação
def create(request):
    if request.method == 'POST':
        form = ProjetosForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'form.html')
    else:
        return render(
            request, 'form.html'
        )
        
# função para a visualização
def view(request, pk):
    data = {}
    data['db'] = Projetos.objects.get(pk=pk)
    return render(request, 'view.html', data)       

# função para a edição
def edit(request, pk):
    data = {}
    data['db'] = Projetos.objects.get(pk=pk)
    data['form'] = ProjetosForm(instance=data['db'])
    return render(request, 'form.html', data)

# função para a atualização
def update(request, pk):
    data = {}
    data['db'] = Projetos.objects.get(pk=pk)
    form = ProjetosForm(request.POST or None, instance=data['db'])
    if form.is_valid:
        form.save()
        return redirect('home')        

# função para a deleção
def delete(request, pk):
    db = Projetos.objects.get(pk=pk)
    db.delete()
    return redirect('home')
         
        
            
       