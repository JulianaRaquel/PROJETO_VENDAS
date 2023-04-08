from django.urls import path

from plataforma.views import categoria

from .views import (add_carrinho, cadastrar_produto, detalhe_produto,
                    remover_carrinho, ver_carrinho)

urlpatterns = [
    path('cadastrar_produto/', cadastrar_produto, name='cadastrar_produto'),
    path('categoria/<int:id>', categoria, name='categoria'),
    path('detalhe_produto/<int:id>', detalhe_produto, name='detalhe_produto'),
    path('add_carrinho/', add_carrinho, name='add_carrinho'),
    path('ver_carrinho/', ver_carrinho, name='ver_carrinho'),
    path('remover-produto/<int:id>', remover_carrinho, name='remover_carrinho'),
]
