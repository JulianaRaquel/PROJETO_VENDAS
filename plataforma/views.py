from django.shortcuts import render, redirect
from produtos.models import Produto, Categoria
from clientes.models import Estado, Endereco
from django.contrib import messages
from django.contrib.messages import constants



def home(request):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'home.html', {'produtos': produtos,
                                         'carrinho': len(request.session['carrinho']),
                                         'categorias': categorias})


def categoria(request, id):
    if not request.session.get('carrinho'):
        request.session['carrinho'] = []
        request.session.save()
    produtos = Produto.objects.filter(categoria_id=id)
    categorias = Categoria.objects.all()
    return render(request, 'home.html', {'produtos': produtos,
                                         'carrinho': len(request.session['carrinho']),
                                         'categorias': categorias})

def perfil(request):
    return render(request, 'perfil.html')


def dados_pessoais(request):
    if request.method == 'GET':
        user = request.user
        enderecos = Endereco.objects.filter(cliente=user)
        estados = Estado.objects.all()
        return render(request, 'dados_pessoais.html', {'estados': estados, 'enderecos': enderecos})
    elif request.method == 'POST':
        rua = request.POST.get('rua')
        complemento = request.POST.get('complemento')
        cep = request.POST.get('cep')
        cidade = request.POST.get('cidade')
        id_estado = request.POST.get('estado')

        if (len(rua.strip()) == 0) or (len(cep.strip()) == 0) or (
                len(cidade.strip()) == 0) or (len(id_estado.strip()) == 0):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/dados_pessoais/')

        if not cep.isnumeric():
            messages.add_message(request, constants.ERROR, 'Digite um CEP válido')
            return redirect('/dados_pessoais/')

        try:
            endereco = Endereco(rua=rua,
                                complemento=complemento,
                                cep=cep,
                                cidade=cidade,
                                estado_id=id_estado,
                                cliente=request.user)

            endereco.save()
            messages.add_message(request, constants.SUCCESS, 'Endereço Cadastrado com Sucesso !!!')
            return redirect('/dados_pessoais')
        except Exception as e:
            print(e)
            return redirect('/dados_pessoais/')


def pedidos(request):
    return render(request, 'pedidos.html')


def finalizar_pedido(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass