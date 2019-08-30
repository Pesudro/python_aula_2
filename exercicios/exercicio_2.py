import unittest

class NumeroString():
    def hmmmm(self):
        while True:
            numero = int(input("Digite um numero entre 1-5:"))
            if numero > 5:
                print("Número inválido")
            elif numero < 1:
                print("Número inválido")
            else:
                break
    def aummm(self, numero):
        if numero == 1:
            return "O numero digitado escrito por extenso é: Um"

        elif numero == 2:
            return "O numero digitado escrito por extenso é: Dois"

        elif numero == 3:
            return "O numero digitado escrito por extenso é: Três"

        elif numero == 4:
            return "O numero digitado escrito por extenso é: Quatro"

        elif numero == 5:
            return "O numero digitado escrito por extenso é: Cinco"



