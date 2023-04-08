from decimal import Decimal
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Produto, Categoria
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required


def cadastrar_produto(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        return render(request, 'cadastrar_produto.html', {'categorias': categorias})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        img = request.FILES.get('arquivo')
        id_categoria = request.POST.get('categoria')
        preco = request.POST.get('preco')
        estoque = request.POST.get('estoque')

        produto = Produto(nome=nome, img=img, categoria_id=id_categoria, preco=preco, estoque=estoque)
        produto.save()
        messages.add_message(request, constants.SUCCESS, 'Produto cadastrado')
        return render(request, 'cadastrar_produto.html')


def detalhe_produto(request, id):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    categorias = Categoria.objects.all()
    prod = Produto.objects.get(id=id)
    return render(
        request,
        'detalhe_produto.html',
        {'produto': prod, 'carrinho': len(request.session['carrinho']), 'categorias': categorias},
    )


def add_carrinho(request):
    carrinho = request.session.setdefault('carrinho', [])
    items_carrinho = {
        item["id_produto"]: item for item in carrinho
    }

    produto = Produto.objects.get(pk=request.POST["id"])
    quantidade = int(request.POST["quantidade"])

    try:
        item = items_carrinho[produto.id]
    except KeyError:  # produto ainda não existe no carrinho
        item = {
            'id_produto': produto.pk,
            'preco': produto.preco,
            'quantidade': quantidade,
            'subtotal': quantidade * produto.preco
        }
        carrinho.append(item)
    else:  # produto já existe, é necessário apenas atualizar
        item['quantidade'] = int(item['quantidade']) + quantidade
        item['subtotal'] = item['quantidade'] * produto.preco

    request.session.modified = True

    return redirect('ver_carrinho')


def ver_carrinho(request):
    carrinho = request.session.get('carrinho', [])
    items = []
    for item in carrinho:
        produto = Produto.objects.get(id=item['id_produto'])
        items.append(
            {
                'img': produto.img.url,
                'nome': produto.nome,
                'quantidade': item['quantidade'],
                'preco': Decimal(item['preco']),
                'subtotal': Decimal(item['subtotal']),
                'id': produto.id,
            }
        )

    total = sum(
        int(item['quantidade']) * Decimal(item['preco']) for item in carrinho
    )
    return render(
        request,
        'ver_carrinho.html',
        {
            'items': items,
            'total': total,
            'categorias': Categoria.objects.all(),
        },
    )


def remover_carrinho(request, id):
    carrinho = request.session.get('carrinho', [])
    request.session['carrinho'] = [
        item for item in carrinho if item['id_produto'] != id
    ]
    return redirect('ver_carrinho')
