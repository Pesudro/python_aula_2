valor = int(input("Digite um numero qualquer aí:"))
if valor >= 0:
    if valor % 2 == 0:
        print("O numero digitado é positivo e par")
    else:
        print("O numero digitado é positivo e impar")
else:
    if valor % 2 == 0:
        print("O numero digitado é negativo e par")
    else:
        print("O numero digitado é negativo e impar")