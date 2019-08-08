"""idade = int(input("Digite a sua idade:"))

def calculo (idade):
    if idade > 18:
        print("Vc tem mais do que 18 anos")
    elif idade == 18:
        print("Vc tem 18 anos")
    else:
        print("VC tem menos do que 18 anos")

calculo(idade)"""

def cria_lista():
    valores = []
    valor = 0

    for i in range(10):
        valor = int(input("Digita um valor aí:"))
        valores.append(valor)

    return valores

def encontra_maior(lista):
    maior_valor = 0
    for i in lista:
        if i > maior_valor:
            maior_valor = i

    return maior_valor


lista = cria_lista()
valor_grandao = encontra_maior(lista)
print("O maior valor é: " + str(valor_grandao))