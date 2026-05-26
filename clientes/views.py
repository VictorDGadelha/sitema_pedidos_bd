from django.shortcuts import render, redirect, get_object_or_404

from .models import Cliente
from .forms import ClienteForm


def criar_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_clientes')
    return render(request, 'clientes/criar_cliente.html', {'form': form})

def listar_clientes(request):
    clientes = Cliente.objects.all()
    
    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('listar_clientes')
    return render(request, 'clientes/editar_clientes.html', {'form': form})

def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('listar_clientes')