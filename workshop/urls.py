# workshop/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                          # ← página inicial
    path('produtosHTML/', views.produtosHTMLFUNC, name='produtosHTML'),
    path('produtosTESTE/', views.produtosTESTEFUNC, name='produtosTESTE'),
    path('vendasTESTE/', views.vendasTESTEFUNC, name='vendasTESTE'),
    path('nova_venda/', views.nova_venda, name='nova_venda'),
    path('lista_vendas/', views.lista_vendas, name='lista_vendas'),  

]