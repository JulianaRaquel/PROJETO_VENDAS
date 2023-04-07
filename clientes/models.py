import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

class Estado(models.Model):
    estado = models.CharField(max_length=15)

    def __str__(self):
        return self.estado

class Users(AbstractUser):

    email = models.EmailField('Endereço de E-mail', unique=True)
    cpf = models.CharField(max_length=16)
    telefone = models.CharField(max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Endereco(models.Model):
    rua = models.CharField(max_length=30)
    complemento = models.CharField(max_length=30)
    cidade = models.CharField(max_length=15)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    cep = models.CharField(max_length=8)
    cliente = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.cep




