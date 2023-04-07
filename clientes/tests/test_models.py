from django.test import TestCase
from ..models import Cliente, Estado, Endereco



class ClienteTestCase(TestCase):

    def setUp(self):
        Cliente.objects.create(usuario='paulo', email='paulo@gmail.com', senha='5050')
        cliente = Cliente.objects.all().first()
        Estado.objects.create(estado='RN')
        estado = Estado.objects.all().first()
        Endereco.objects.create(rua='dias alves', numero=20, cep='101020', cidade='Natal', estado=estado, cliente=cliente)

    def test_create_banco(self):
        cliente = Cliente.objects.get(usuario='paulo')

        self.assertEqual(cliente.__str__(), 'paulo')

    def test_create_banco_tabela_endereco(self):
        endereco = Endereco.objects.get(cep='101020')

        self.assertEqual(endereco.__str__(), '101020')

    def test_tabela_estado(self):
        estado = Estado.objects.get(estado='RN')

        self.assertEqual(estado.__str__(), 'RN')



