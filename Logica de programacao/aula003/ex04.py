"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
Quantas vezes apareceu o número 9;
Em que posição foi digitado o primeiro valor 3;
Quais foram os números pares.
"""
values = []
valuesTuple = ()

for i in range(4):
    value = int(input('informe um numero: '))
    values.append(value)

valuesTuple = values

VezesNove = 0

for c in valuesTuple:
    if c == 9:
        VezesNove += 1

print(f'O numero nove apareceu {VezesNove}')

for i, c in enumerate (valuesTuple):
    if c == 3:
        print(i+1)

for c in valuesTuple:
    if c % 2 == 0:
        print(f'O numero {c} é par')







