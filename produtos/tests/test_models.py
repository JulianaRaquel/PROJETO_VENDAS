from django.test import TestCase
from produtos.models import Produto, Categoria

class ProdutoTestCase(TestCase):

    def setUp(self):
        Categoria.objects.create(categoria='bebidas')
        categoria = Categoria.objects.all().first()
        Produto.objects.create(nome='coca', categoria=categoria, preco=10, estoque=100)

    def test_create_banco(self):
        produto = Produto.objects.get(nome='coca')

        self.assertEqual(produto.__str__(), 'coca')

    def test_add_desconto(self):
        produto = Produto.objects.get(nome='coca')
        produto.add_desconto()
        self.assertEqual(produto.desconto, -3)

    def test_categoria_str(self):
        categoria = Categoria.objects.get(categoria='bebidas')

        self.assertEqual(categoria.__str__(), 'bebidas')
