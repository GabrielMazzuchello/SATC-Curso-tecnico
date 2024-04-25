import math
soma = 0
maior = 0
menor = math.inf
digitos = 0
while True:
    numero = int(input('Informe um numero: '))
    if numero < 0:
        break
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
        digitos = digitos + 1
        soma += numero

media = soma / digitos
print('A média é {:.2f} e o numero maior digitado é {} e o menor é {}'.format(media, maior, menor))
