"""Crie um programa que leia uma lista de números e retorne uma lista com os números divisíveis
por 5, usando filter e uma função lambda."""

listaNumeros = []

for c in range(5):
    num = float(input('Informe um numero: '))
    listaNumeros.append(num)

numDivisiv = list(filter(lambda x : x % 5 == 0, listaNumeros))
print(numDivisiv)

    