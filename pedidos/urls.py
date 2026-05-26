from django.urls import path

from .views import *

urlpatterns = [

    path('', listar_pedidos, name='listar_pedidos'),

    path('criar/', criar_pedido, name='criar_pedido'),

    path('<int:id>/', detalhes_pedido, name='detalhes_pedido'),

    path('item/excluir/<int:id>/', excluir_item_pedido, name='excluir_item'),
    
    path('relatorio/', relatorio_vendas, name='relatorio_vendas'),
    
]