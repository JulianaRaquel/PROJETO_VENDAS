from .views import cadastrar_funcionario
from django.urls import path


urlpatterns = [
    path('cadastrar_funcionario/', cadastrar_funcionario, name='cadastrar_funcionario'),
]