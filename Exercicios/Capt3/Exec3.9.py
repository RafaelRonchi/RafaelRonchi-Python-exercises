#Escreva um programa que leia a quantidade de dias, horas, minutos
#e segundos do usuário. Calcule o total em segundos

dia = float(input("Digite o valor em dias "))
horas = float(input("Digite o valor em horas "))
segundo = float(input("Digite o valor em minutos: "))

dia = dia*86400
horas = horas*3600
segundos = horas*60

valor=(dia+horas+segundo)

print("Valores em segundos %.2f"%valor)