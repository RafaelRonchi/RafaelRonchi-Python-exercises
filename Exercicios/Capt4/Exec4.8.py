#Escreva um programa que leia dois números e que pergunte qual
#operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-),
#multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.


n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print(" ")
print("1: + ")
print("2: - ")
print("3: * ")
print("4: / ")
print(" ")
n = float(input("Escolha a operação (1,2,3 ou 4): "))

if n == 1:
    x = n1 + n2
    print(" %.2f + %.2f : %.2f" % (n1, n2, x))
elif n == 2:
    x = n1 - n2
    print(" %.2f - %.2f : %.2f" % (n1, n2, x))
elif n == 3:
    x = n1 * n2
    print(" %.2f * %.2f : %.2f" % (n1, n2, x))
elif n == 4:
    x = n1 / n2
    print(" ")
    print(" %.2f / %.2f : %.2f" % (n1, n2, x))
if n > 4 or n < 1:
    print("ERRO! NÚMERO INVALIDO")
