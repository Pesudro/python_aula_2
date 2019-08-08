"""resposta = 42

pergunta = "Qual a resposta para a vida, o universo e td mais?"

print(pergunta)
print("a resposta é: " + str(resposta))"""


def calculo(n1, n2):
    if n1 > 10:
        print("Caracaca mermão, a sua nota na n1 foi maior que 10")
    elif n1 == 10:
        print("Caracaca mermão, a sua nota na n1 foi igual a 10")
    else:
        print("Caracaca mermão, a sua nota na n1 foi menor que 10")

    return n1 + n2


result = calculo(11, 7)
print("Soma da n1 com a n2: " + str(result))