"""13 - Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres
(considere que as idades dos homens serão sempre diferentes entre si, bem como as das mulheres).
Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova,
e o produto das idades do homem mais novo com a mulher mais velha."""

idadeHomem1 = int(input("Digite a idade do primeiro homem:"))
while True:
    idadeHomem2 = int(input("Digite do segundo homem, não podendo ser igual ao primeiro:"))
    if idadeHomem1 != idadeHomem2:
        break
    print("Favor digitar um valor diferente do primeiro digitado.")

idadeMulher1 = int(input("Digite a idade da primeira mulher:"))
while True:
    idadeMulher2 = int(input("Digite a idade da segunda mulher, não podendo ser igual a primeira:"))
    if idadeMulher1 != idadeMulher2:
        break
    print("Favor digitar um valor diferente do primeiro digitado.")

if idadeHomem1 > idadeHomem2:
    homemVelho = idadeHomem1
    homemNovo = idadeHomem2
else:
    homemVelho = idadeHomem2
    homemNovo = idadeHomem1

if idadeMulher1 > idadeMulher2:
    mulherVelha = idadeMulher1
    mulherNova = idadeMulher2
else:
    mulherVelha = idadeMulher2
    mulherNova = idadeMulher1

soma = homemVelho + mulherNova
produto = homemNovo*mulherVelha

print("Soma das idades do homem mais velho com a mulher mais nova: ",soma)
print("Produto das idades do homem mais novo com a mulher mais velha:",produto)
