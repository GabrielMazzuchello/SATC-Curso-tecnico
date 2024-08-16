# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar para cada palavra, quais são as suas vogais.

words = ("armagedom", "feijao", "arroz", "leite", "pao")

for c in words:
    letras = []
    for i in c:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            letras.append(i)
    print(f'A palavra {c} tem as vogais {letras}')