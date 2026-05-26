from django.contrib import admin
from pedidos.models import Pedido, ItemPedido

admin.site.register(Pedido)
admin.site.register(ItemPedido)