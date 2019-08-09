numeros = []
soma = 0

for i in range(10):
    numero = int(input("\n Digite um numero:"))
    numeros.append(numero)
    soma = soma + numero


numeros.sort()
maior_numero = numeros[9]
menor_numero = numeros[0]
media_aritmetica = soma/10

print("\nMaior numero: ", maior_numero)
print("Menor numero: ", menor_numero)
print("Soma dos numeros:", soma)
print("Média aritmética dos numeros: ", media_aritmetica)