#Faça um programa que calcule o aumento de um salário. Ele deve
#solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento
#e do novo salário.

sal = float(input("Digite o sálario: "))
if sal>1250.00:
    sal=(sal*0.10)+sal
elif sal<=1250.00:
    sal=(sal*0.15)+sal

print("Valor final %.2f " % sal )