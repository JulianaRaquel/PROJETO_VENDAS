from produtos.models import Produto
from django.db import models
from clientes.models import Users
from clientes.models import Endereco, Estado

class Pagamento(models.Model):
    pagamento = models.CharField(max_length=15)

    def __str__(self):
        return self.pagamento


class Pedido(models.Model):
    numero_pedido = models.CharField(max_length=30)
    cliente = models.ForeignKey(Users, on_delete=models.CASCADE)
    itens_do_pedido = models.ManyToManyField(Produto)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    total = models.FloatField()
    pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.cliente

class ItemDoPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco = models.FloatField()

    def __str__(self):
        return self.pedido
