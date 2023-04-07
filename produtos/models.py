from django.db import models


class Categoria(models.Model):
    categoria = models.CharField(max_length=30)

    def __str__(self):
        return self.categoria

class Produto(models.Model):
    nome = models.CharField(max_length=15)
    img = models.ImageField(upload_to='foto_produto', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.FloatField()
    estoque = models.IntegerField()
    desconto = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

    def add_desconto(self):
        self.desconto -= 3


