# workshop/admin.py
from django.contrib import admin
from .models import Seccao, Produto, Venda, VendeSe

@admin.register(Seccao)
class SeccaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'qtd', 'desconto', 'iva', 'seccao')
    search_fields = ('nome',)
    list_filter = ('seccao', 'iva')

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('recibo', 'total', 'data')
    list_filter = ('data',)

@admin.register(VendeSe)
class VendeSeAdmin(admin.ModelAdmin):
    list_display = ('venda', 'produto', 'qtd', 'preco')