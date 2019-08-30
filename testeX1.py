import unittest

from exercicios.exercicio_1 import calculo


class calculoTeste(unittest.TestCase):

    def test_louco(self):
        calc = calculo()
        resultado = calc.maior_idade(18)
        self.assertEqual(resultado, "Vc tem 18 anos")