#Escreva uma expressão para determinar se uma pessoa deve ou não
#pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que
#R$ 1.200,00.

salario = float(input('Informe o salario: '))

if salario > 1200.00:
    print('Sim, você deve pagar imposto!')
else :
    print('Não, você não deve pagar imposto!')
