import unittest

class calculo():

    def __init__(self):
        self.idade = 0

    def calculo(self, idade):
        try:
            self.idade = int(input("Digite a sua idade:"))
        except ValueError:
            print("Valor inválido.")

        print(self.maior_idade(self.idade))

    def maior_idade(self, idade):
        if idade > 18:
            return "Vc tem mais do que 18 anos"
        elif idade == 18:
            return "Vc tem 18 anos"
        else:
            return "VC tem menos do que 18 anos"


