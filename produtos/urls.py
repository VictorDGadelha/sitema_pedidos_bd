from django.urls import path

from .views import *

urlpatterns = [
    path(
        'categorias/',
        listar_categorias,
        name='listar_categorias'
    ),

    path(
        'categorias/criar/',
        criar_categoria,
        name='criar_categoria'
    ),

    path(
        'categorias/editar/<int:id>/',
        editar_categoria,
        name='editar_categoria'
    ),

    path(
        'categorias/excluir/<int:id>/',
        excluir_categoria,
        name='excluir_categoria'
    ),

    path(
        '',
        listar_produtos,
        name='listar_produtos'
    ),

    path(
        'criar/',
        criar_produto,
        name='criar_produto'
    ),

    path(
        'editar/<int:id>/',
        editar_produto,
        name='editar_produto'
    ),

    path(
        'excluir/<int:id>/',
        excluir_produto,
        name='excluir_produto'
    ),
]