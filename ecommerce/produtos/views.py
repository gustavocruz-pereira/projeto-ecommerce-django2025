from django.shortcuts import render, get_object_or_404
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.filter(disponivel=True)
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'produtos/detalhe_produto.html', {'produto': produto})

def pagina_inicial(request):
    produtos = Produto.objects.filter(disponivel=True)
    return render(request, 'produtos/inicio.html', {'produtos': produtos})

