from django import forms
from .models import (Produto, Categoria)

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'nome',
            'descricao',
            'preco',
            'estoque',
            'categoria',
            'ativo'
        ]
        
        widgets = {

            'nome': forms.TextInput(attrs={'class': 'form-control'}),

            'descricao': forms.Textarea(attrs={'class': 'form-control'}),

            'preco': forms.NumberInput(attrs={'class': 'form-control'}),

            'estoque': forms.NumberInput(attrs={'class': 'form-control'}),

            'categoria': forms.Select(attrs={'class': 'form-select'}),

            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
        }
