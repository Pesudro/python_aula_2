"""12 - Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles"""

valor1 = int(input("Digite um valor:"))
while True:
    valor2 = int(input("Digite outro valor, não podendo ser igual ao primeiro valor digitado:"))
    if valor2 != valor1:
        break
    print("Favor digitar um valor diferente do primeiro digitado.")

if valor1 > valor2:
    print("O maior valor digitado foi o primeiro(",valor1,")")
else:
    print("O maior valor digitado foi o segundo(", valor2, ")")
