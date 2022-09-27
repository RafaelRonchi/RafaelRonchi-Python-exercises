#Escreva uma expressão que será utilizada para decidir se um aluno foi
#ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores
#que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma
#está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3

materia1 = int(input('Informe a nota da matéria 1: '))
materia2 = int(input('Informe a nota da matéria 2: '))
materia3 = int(input('Informe a nota da matéria 3: '))
print('Media: ',(materia1+materia2+materia3)/3)
if (((materia1+materia2+materia3)/3)>=7):
    print('Aprovado')
else: 
    print('Reprovado')