from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from .models import Users
from django.contrib import auth

def cadastrar_cliente(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = Users.objects.filter(username=usuario)

        if user:
            messages.add_message(request, constants.ERROR, 'Este usuário já existe')
            return redirect('/cadastrar_cliente/')

        mail = Users.objects.filter(email=email)

        if mail:
            messages.add_message(request, constants.ERROR, 'Este e-mail já está cadastrado')
            return redirect('/cadastrar_cliente/')

        try:
            cliente = Users(username=usuario, email=email)
            cliente.set_password(senha)  # essa linha salva a senha do jeito certo no BD
            cliente.save()

            messages.add_message(request, constants.SUCCESS, 'Cliente cadastrado !!!')
            return redirect('/cadastrar_cliente/')

        except:
            messages.add_message(request, constants.WARNING, 'Erro interno do sistema')
            return redirect('/cadastrar_cliente/')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, email=email, password=senha)

        if not user:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos !!!')
            return redirect('/login')
        else:
            # se o usuário existe no banco de dados, pe feita a autenticação do usuário abaixo
            auth.login(request, user)
            return redirect('/home')

