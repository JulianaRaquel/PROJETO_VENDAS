from django.db import models


class Cargo(models.Model):
    cargo = models.CharField(max_length=15)

    def __str__(self):
        return self.cargo


class Funcionario(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=16)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    salario = models.FloatField()

    def __str__(self):
        return self.nome



