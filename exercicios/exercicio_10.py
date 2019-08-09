n1 = int(input("Digite a nota da n1:"))
n2 = int(input("Digite a nota da n2:"))
n3 = int(input("Digite a nota da n3"))

soma = n1+n2+n3
media = soma/3

if media >= 7:
    print("\n Considerando que a média é 7, o seu status é: aprovado")
else:
    print("\n Considerando que a média é 7, o seu status é: reprovado")