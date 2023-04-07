from django.test import TestCase
from ..models import Cargo, Funcionario


class FuncionarioTestCase(TestCase):

    def setUp(self):
        Cargo.objects.create(cargo='vendedor')
        cargo = Cargo.objects.all().first()
        Funcionario.objects.create(nome='cesar', cpf='2222', cargo=cargo, salario=2000)

    def test_create_banco(self):
        funcionario = Funcionario.objects.get(nome='cesar')

        self.assertEqual(funcionario.__str__(), 'cesar')

    def test_cargo_str(self):
        funcionario = Funcionario.objects.get(cargo__cargo='vendedor')

        self.assertEqual(funcionario.cargo.__str__(), 'vendedor')