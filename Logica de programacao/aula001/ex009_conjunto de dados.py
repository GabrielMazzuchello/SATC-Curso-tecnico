"""Tem-se um conjunto de dados contendo a altura e o sexo (masculino, feminino) de
50 pessoas. Fazer um algoritmo que calcule e escreva:
a. a maior e a menor altura do grupo;
b. a média de altura das mulheres;
c. o número de homens;
d. A porcentagem de homens e de mulheres"""

men = 0
PercentageMen = 0
women = 0
PercentageWomen = 0
FemaleHeight = 0
AverageFemaleHeight = 0
GreaterHeight = 0
ShortestHeight = 9999

for i in range(10):
    height = float(input('Informe sua altura: '))
    if height > GreaterHeight:
        GreaterHeight = height

    if height < ShortestHeight:
        ShortestHeight = height
 
    sexo = input('Informe seu sexo (F/M)').upper().strip()[0]

    if sexo == 'F':
        women += 1
        FemaleHeight += height
        AverageFemaleHeight = FemaleHeight / women

    elif sexo == 'M':
        men += 1

    PercentageMen = men / 10 * 100
    PercentageWomen = women / 10 * 100

print(f'A maior altura é de {GreaterHeight} e a menor é de {ShortestHeight}')
print(f'A media de altura das mulheres é de {AverageFemaleHeight}')
print(f'O numero de homens é {men}')
print(f'A porcentagem de homens é {PercentageMen}% e de mulheres é de {PercentageWomen}%')