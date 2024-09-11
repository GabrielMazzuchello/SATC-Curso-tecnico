"""Crie um programa que receba uma lista de palavras e, usando filter() com uma expressão
lambda, filtre apenas as palavras que possuem mais de três letras. Depois, utilizando map(), crie
uma nova lista contendo o número de caracteres de cada palavra filtrada"""

listaPalavras = []

for c in range(5):
    palavra = input('Informe uma palavra: ')
    listaPalavras.append(palavra)

lista = list(filter(lambda x : len(x) > 3, listaPalavras))
listaOrdenada = list(map(lambda x : len(x), lista))
print(listaOrdenada)

