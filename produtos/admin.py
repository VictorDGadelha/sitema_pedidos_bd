from django.contrib import admin
from produtos.models import Categoria, Produto

admin.site.register(Categoria)
admin.site.register(Produto)