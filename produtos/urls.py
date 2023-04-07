from .views import cadastrar_produto, detalhe_produto, ver_carrinho, add_carrinho
from plataforma.views import categoria
from django.urls import path


urlpatterns = [
    path('cadastrar_produto/', cadastrar_produto, name='cadastrar_produto'),
    path('categoria/<int:id>', categoria, name='categoria'),
    path('detalhe_produto/<int:id>', detalhe_produto, name='detalhe_produto'),
    path('add_carrinho/', add_carrinho, name='add_carrinho'),
    path('ver_carrinho/', ver_carrinho, name="ver_carrinho"),
]