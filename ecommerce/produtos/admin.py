from django.contrib import admin
from .models import Categoria, Produto

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    prepopulated_fields = {"slug": ("nome",)}

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'estoque', 'disponivel', 'categoria']
    list_filter = ['disponivel', 'categoria']
    search_fields = ['nome', 'descricao']