class Calculadora():

    def soma(self, num1, num2):
        return num1 + num2

    def subtracao(self, num1, num2):
        return num1 - num2

    def multiplicacao(self, num1, num2):
        return num1*num2

    def divisao(self, num1, num2):
        return num1/num2


calculadoraXRL8 = Calculadora()

while True:
    print("-- Operações --\n")
    print("1 - Soma")
    print("2 - Substração")
    print("3 - Divisão")
    print("4 - Multiplicação")
    print("5 - Desligar calculadora")
    op = int(input("\nDigite o numero da operação que vc deseja realizar:"))

    if op == 1:
        print("-- SOMA --\n")
        num1 = int(input("Digite o primeiro valor desejado:"))
        num2 = int(input("Digite o segundo valor desejado:"))
        print("\nResultado da soma: " + str(calculadoraXRL8.soma(num1, num2)))
        opc = input("\n Deseja continuar fazendo operações na calculadora? SIM ou NAO:\n")
        if opc.upper() == "NAO":
            break

    if op == 2:
        print("-- SUBTRAÇÃO --\n")
        num1 = int(input("Digite o primeiro valor desejado:"))
        num2 = int(input("Digite o segundo valor desejado:"))
        print("\nResultado da divisao: " + str(calculadoraXRL8.subtracao(num1, num2)))
        opc = input("\n Deseja continuar fazendo operações na calculadora? SIM ou NAO:\n")
        if opc.upper() == "NAO":
            break

    if op == 4:
        print("-- MULTIPLICAÇÃO --\n")
        num1 = int(input("Digite o primeiro valor desejado:"))
        num2 = int(input("Digite o segundo valor desejado:"))
        print("\nResultado da multiplicação: " + str(calculadoraXRL8.multiplicacao(num1, num2)))
        opc = input("\n Deseja continuar fazendo operações na calculadora? SIM ou NAO:\n")
        if opc.upper() == "NAO":
            break

    if op == 3:
        print("-- DIVISÃO --\n")
        num1 = int(input("Digite o primeiro valor desejado:"))
        num2 = int(input("Digite o segundo valor desejado:"))
        print("\nResultado da divisão: " + str(calculadoraXRL8.divisao(num1, num2)))
        opc = input("\n Deseja continuar fazendo operações na calculadora? SIM ou NAO:\n")
        if opc.upper() == "NAO":
            break

    if op == 5:
        break




