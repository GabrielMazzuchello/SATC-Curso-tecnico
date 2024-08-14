""" 
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 
           'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezesseis', 'dezenove', 'vinte')

number = int(input('informe um numero: '))
print(f'O numero por extenso é: {numbers[number]}')

