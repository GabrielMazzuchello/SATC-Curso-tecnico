# Escreva um programa que calcule a média de uma lista de números usando a função reduce.
import functools
numbersList = []

for c in range(5):
    numbers = float(input('Informe um numero: '))
    numbersList.append(numbers)

soma = functools.reduce(lambda x, y : x + y, numbersList)
media = soma / len(numbersList)

print(f'a soma é {soma}')
print(f'A média é {media}')
