"""Implemente uma função que receba uma lista de numeros e retorne apenas os numeros pares usando filter e uma função lambda"""

numbersList = []

for c in range(5):
    numbers = float(input('Informe um numero: '))
    numbersList.append(numbers)

print(list(filter(lambda x : x % 2 == 0, numbersList)))