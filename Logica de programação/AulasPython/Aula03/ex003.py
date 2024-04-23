for c in range(11):
    maior = 0
    menor = 0
    numero = int(input('Informe um numero inteiro: '))

    if numero > maior:
        maior = numero

    elif numero < menor:
        menor = numero

print('O maior numer é {} e o menor numero é {}'.format(maior, menor))