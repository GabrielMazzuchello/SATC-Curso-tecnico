while True:
    numero = int(input('Informe um valor: '))
    if numero % 2 == 0:
        print('O numero {} é par'.format(numero))
    elif numero % 2 != 0:
        print('O numero {} é inpar'format(numero))
    elif numero == 0:
        break