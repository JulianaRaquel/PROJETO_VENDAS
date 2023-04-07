from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render, redirect
from .models import Funcionario, Cargo


def cadastrar_funcionario(request):
    if request.method == 'GET':
        cargos = Cargo.objects.all()
        return render(request, 'cadastrar_funcionario.html', {'cargos': cargos})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        id_cargo = request.POST.get('cargo')
        salario = request.POST.get('salario')

        funcionario = Funcionario(nome=nome, cpf=cpf, cargo_id=id_cargo, salario=salario)
        funcionario.save()

        messages.add_message(request, constants.SUCCESS, 'Funcionário Cadastrado')
        return redirect('/cadastrar_funcionario/')

