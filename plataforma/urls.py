from .views import home, perfil, dados_pessoais, pedidos, finalizar_pedido
from django.urls import path


urlpatterns = [
    path('home/', home, name='home'),
    path('perfil/', perfil, name='perfil'),
    path('dados_pessoais/', dados_pessoais, name='dados_pessoais'),
    path('pedidos/', pedidos, name='pedidos'),
    path('finalizar_pedido/', finalizar_pedido, name="finalizar_pedido"),
]