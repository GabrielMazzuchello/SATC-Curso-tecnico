n1 = float(input('infome um numero: '))
n2 = float(input('informe outro numero: '))

if n1 > n2:
    print('o numero {} é maior que o numero {}'.format(n1, n2))
elif n2 > n1:
    print('o numero {} é maior que o numero {}'.format(n2, n1))
elif n2 == n1:
    print('Os numeros informados são iguais')
else:
    print('numero invalido')
