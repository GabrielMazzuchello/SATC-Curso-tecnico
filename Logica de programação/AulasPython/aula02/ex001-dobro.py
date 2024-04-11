#1.	Faça um script que leia um número e mostre o seu dobro, seu triplo e a sua raiz quadrada.
import math
n1 = input('Informe umm numero: ')

dobro = n1 * 2
triplo = n1 * 3
raiz = (n1 ** (1/2))

print('o dobro é {} o triplo é {} e a rais quadrada é {}'.format(dobro, triplo, raiz))