while True:
    numero = int(input('Informe um valor: '))
    if  numero == 0:
        break
    elif numero % 2 != 0:
        print('O número {} é ímpar'.format(numero))
    elif numero % 2 == 0:
        print('O número {} é par'.format(numero))