import math
vetor = [0]*10
for i in range(10):
    vetor[i] = input('Digite um valor: ')

maior = vetor[0]    
menor = vetor[0]

for i in range(0, 10):
    if vetor[i] > maior:
        maior = vetor[i]
    elif vetor[i] < menor:
        menor = vetor[i]
print('O maior numero é: {}'.format(maior))
print('O menor numero é: {} '.format(menor))