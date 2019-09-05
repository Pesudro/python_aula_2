import unittest

from exercicios.exercicio_3 import Calculadora


class CalculoTeste(unittest.TestCase):

    def test_doido(self):
        calc = Calculadora()
        resultado = calc.divisao(20, 4)
        self.assertEqual(resultado, 5)
