idade = int(input("Digite a sua idade:"))

def calculo (idade):
    if idade > 18:
        print("Vc tem mais do que 18 anos")
    elif idade == 18:
        print("Vc tem 18 anos")
    else:
        print("VC tem menos do que 18 anos")

calculo(idade)