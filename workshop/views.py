import json

from django.shortcuts import render

# Create your views here.
# workshop/views.py
from django.shortcuts import render
from .models import  Produto, Venda
import json

def produtosHTMLFUNC(request):
    return render(request, 'produtosHTML.html', {})

def produtosTESTEFUNC(request):
    produtos = Produto.objects.all()
    return render(request, 'produtosTESTE.html', {'produtos': produtos})

def vendasTESTEFUNC(request):
    vendas = Venda.objects.all()
    return render(request, 'vendasTESTE.html', {'vendas': vendas})


import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Produto, Venda, VendeSe

def nova_venda(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        itens = dados.get('itens', [])

        # calcula o total
        total = sum(item['preco'] * item['qty'] for item in itens)

        # cria a venda
        import datetime
        recibo = dados.get('recibo')
        venda = Venda.objects.create(
            recibo=recibo,
            total=round(total, 2),
            data=datetime.date.today()
        )

        # cria as linhas e desconta o stock
        for item in itens:
            produto = Produto.objects.get(id=item['id'])

            # verifica se há stock suficiente
            if produto.qtd < item['qty']:
                return JsonResponse({'erro': f'Stock insuficiente para {produto.nome}'}, status=400)

            # cria linha na tabela vende_se
            VendeSe.objects.create(
                venda=venda,
                produto=produto,
                qtd=item['qty'],
                preco=item['preco']
            )

            # desconta o stock
            produto.qtd -= item['qty']
            produto.save()

        return JsonResponse({'sucesso': True, 'recibo': recibo})

    # GET — mostra a página
    produtos_lista = []
    for p in Produto.objects.all():
        produtos_lista.append({
            'id': p.id,
            'nome': p.nome,
            'preco': float(p.preco),
            'qtd': p.qtd,
            'desconto': p.desconto,
            'iva': p.iva,
            'seccao': p.seccao_id,
        })

    return render(request, 'nova_venda.html', {
        'produtos_json': json.dumps(produtos_lista)
    })

def home(request):
    return render(request, 'home.html', {})

def lista_vendas(request):
    vendas = Venda.objects.all().order_by('-data')
    return render(request, 'lista_vendas.html', {'vendas': vendas})
