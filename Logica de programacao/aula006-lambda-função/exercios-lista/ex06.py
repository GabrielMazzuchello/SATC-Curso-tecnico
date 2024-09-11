"""Escreva um programa que leia uma lista de strings e retorne uma lista com as strings ordenadas
pelo comprimento, usando sorted e uma função lambda."""

listaPalavras = []

for c in range(5):
    palavra = input('Informe uma palavra: ')
    listaPalavras.append(palavra)

ordered = sorted(listaPalavras, key=lambda x : len(x))
print(ordered)