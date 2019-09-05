import unittest

from exercicios.exercicio_2 import NumeroString


class TesteDoido(unittest.TestCase):

    def test_ahhh(self):
        aaaa = NumeroString()
        resultado = aaaa.aummm(3)
        self.assertEqual(resultado, "O numero digitado escrito por extenso é: Três")