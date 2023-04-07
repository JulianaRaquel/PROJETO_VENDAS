from .views import cadastrar_cliente, login
from django.urls import path


urlpatterns = [
    path('', cadastrar_cliente),
    path('cadastrar_cliente/', cadastrar_cliente, name='cadastrar_cliente'),
    path('login/', login, name='login'),
]