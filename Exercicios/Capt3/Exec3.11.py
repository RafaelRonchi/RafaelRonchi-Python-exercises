#Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

merc = float(input("Digite o valor da mercadoria: "))
print(" ")
desc = float(input("Digite o percentual de desconto: "))
desc = desc/100
desconto=merc*desc
merc=merc-desconto
print(" ")
print("O valor de desconto é de: %.2f"%desc)
print("O valor final é de: %.2f"%merc)