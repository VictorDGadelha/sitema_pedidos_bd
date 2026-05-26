from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=100, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    estoque = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')
    
    ativo = models.BooleanField(default=True)
    def __str__(self):
        return self.nome
    
        