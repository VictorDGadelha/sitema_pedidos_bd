from django.shortcuts import (render, redirect, get_object_or_404)
from .models import (Categoria, Produto)
from .forms import (CategoriaForm, ProdutoForm)

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'produtos/categorias/listar_categorias.html', {'categorias': categorias})

def criar_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_categorias')
    return render(request, 'produtos/categorias/criar_categoria.html', {'form': form})

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if form.is_valid():
        form.save()
        return redirect('listar_categorias')
    return render(request, 'produtos/categorias/editar_categoria.html', {'form': form})

def excluir_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('listar_categorias')

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/produtos/listar_produtos.html', {'produtos': produtos})

def criar_produto(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_produtos')
    return render(request, 'produtos/produtos/criar_produto.html', {'form': form})

def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('listar_produtos')
    return render(request, 'produtos/produtos/editar_produto.html', {'form': form})

def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('listar_produtos')
    