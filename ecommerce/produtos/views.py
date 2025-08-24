from django.shortcuts import render
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.filter(disponivel=True)
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})
