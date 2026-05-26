from decimal import Decimal

from django.shortcuts import (render, redirect, get_object_or_404)
from .models import (Pedido, ItemPedido)
from .forms import (PedidoForm, ItemPedidoForm)
from django.db import connection

def listar_pedidos(request):
    pedidos = Pedido.objects.all().order_by('-data_pedido')
    return render(request, 'pedidos/listar_pedidos.html', {'pedidos': pedidos})

def criar_pedido(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        pedido = form.save(commit=False)
        pedido.valor_total = 0.00
        pedido.save()
        return redirect('detalhes_pedido', pedido.id)
    return render(request, 'pedidos/criar_pedido.html', {'form': form})

def detalhes_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    itens = pedido.itens.all()
    form = ItemPedidoForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            item = form.save(commit=False)
            
            if item.quantidade > item.produto.estoque:
                return render(
                    request,
                    'pedidos/detalhes_pedido.html',
                    {
                        'pedido': pedido,
                        'itens': itens,
                        'form': form,
                        'erro': 'Estoque insuficiente!'
                    }
                )
            
            item.pedido = pedido
            item.subtotal = (item.produto.preco * item.quantidade)
            item.save()
            produto = item.produto
            produto.estoque -= item.quantidade
            produto.save()
            atualizar_total_pedido(pedido)
            
            return redirect('detalhes_pedido', pedido.id)

    return render(
        request, 
        'pedidos/detalhes_pedido.html', 
        {
            'pedido': pedido, 
            'itens': itens, 
            'form': form
        }
    )

def excluir_item_pedido(request, id):
    item = get_object_or_404(ItemPedido, id=id)
    pedido = item.pedido
    item.delete()
    atualizar_total_pedido(pedido)
    return redirect('detalhes_pedido', pedido.id)

def atualizar_total_pedido(pedido):
    total = Decimal('0.00')
    for item in pedido.itens.all():
        total += item.subtotal
    pedido.valor_total = total
    pedido.save()

def relatorio_vendas(request):
    cliente = request.GET.get('cliente', '')
    status = request.GET.get('status', '')
    produto = request.GET.get('produto', '')

    query = """ SELECT * FROM relatorio_vendas WHERE 1=1 """

    parametros = []

    if cliente:

        query += """ AND cliente ILIKE %s """

        parametros.append(f'%{cliente}%')

    if status:

        query += """ AND status = %s """

        parametros.append(status)

    if produto:

        query += """ AND produto ILIKE %s """

        parametros.append(f'%{produto}%')

    query += """ ORDER BY data_pedido DESC """

    with connection.cursor() as cursor:

        cursor.execute(query, parametros)

        colunas = [col[0] for col in cursor.description]

        relatorio = [dict(zip(colunas, row)) for row in cursor.fetchall()]
        
    return render(request,'pedidos/relatorio_pedido.html',{'relatorio': relatorio})
        