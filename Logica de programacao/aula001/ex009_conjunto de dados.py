"""Tem-se um conjunto de dados contendo a altura e o sexo (masculino, feminino) de
50 pessoas. Fazer um algoritmo que calcule e escreva:
a. a maior e a menor altura do grupo;
b. a média de altura das mulheres;
c. o número de homens;
d. A porcentagem de homens e de mulheres"""
men = 0
women = 0
GreaterHeight = 0
for i in range(2):
    height = float(input('Informe sua altura: '))
    if height > GreaterHeight:
        GreaterHeight == height

        
    sexo = input('Informe seu sexo (F/M)').upper().strip()[0]

    if sexo == 'F':
        women += 1
    elif sexo == 'M':
        men += 1

    