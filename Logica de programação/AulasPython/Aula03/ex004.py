numero = int(input('Informe um numero: '))
fatorial = 1
while (numero > 0):
    fatorial = fatorial * numero
    numero -= 1

print('O resultado é: {}'.format(fatorial))