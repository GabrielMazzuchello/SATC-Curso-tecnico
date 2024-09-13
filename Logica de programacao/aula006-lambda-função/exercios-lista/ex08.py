"""Implemente uma função que receba uma lista de números inteiros e retorne o produto de todos
os números da lista usando a função reduce() e uma expressão lambda """
import functools

listaNumeros = []

for c in range(5):
    num = int(input('Informe um numero: '))
    listaNumeros.append(num)

produto = functools.reduce(lambda x,y : x*y, listaNumeros)
print(produto)