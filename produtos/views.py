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
    return render(request, 'detalhe_produto.html', {'prod': prod,
                                                    'carrinho': len(request.session['carrinho']),
                                                    'categorias': categorias})





def add_carrinho(request):
    # verifica se a session carrinho existe. Se não existir ele cria essa variável e salva
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    # aqui está pegando tudo que foi enviado do formulário de detalhe_produto.html e convertendo para um dicionário do python
    x = dict(request.POST)

    id = int(x['id'][0])
    total = Produto.objects.filter(id=id)[0].preco


    total *= int(x['quantidade'][0])
    data = {'id_produto': int(x['id'][0]),
            'preco': total,
            'quantidade': x['quantidade'][0]}

    request.session['carrinho'].append(data)
    request.session.modified = True
    # return HttpResponse(request.session['carrinho'])
    return redirect('/ver_carrinho/')


def ver_carrinho(request):
    categorias = Categoria.objects.all()
    dados_mostrar = []
    for i in request.session['carrinho']:
        prod = Produto.objects.filter(id=i['id_produto'])
        dados_mostrar.append(
            {'img': prod[0].img.url,
             'nome': prod[0].nome,
             'quantidade': i['quantidade'],
             'preco': i['preco'],
             'id': i['id_produto']
             }
        )
    total = sum([float(i['preco']) for i in request.session['carrinho']])

    return render(request, 'ver_carrinho.html', {'dados': dados_mostrar,
                                             'total': total,
                                             'carrinho': len(request.session['carrinho']),
                                             'categorias': categorias,
                                        })

