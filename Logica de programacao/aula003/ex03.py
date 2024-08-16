# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tuplas. Depois disso, mostre a listagem de 
# números gerados e indique o menor e o maior valor que estão na tupla.

import random

numbers = []
numberTuple = ()

for c in range(5):
    aleatorio = random.randint(0, 100000000)
    numbers.append(aleatorio)

numberTuple = numbers

minNunbers = min(numbers)
maxNunbers = max(numbers)

print(numberTuple)
print(f'O maior valor da tupla é {maxNunbers}')
print(f'O menor valor da tupla é {minNunbers}')