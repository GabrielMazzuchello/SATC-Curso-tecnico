#3.	Faça um programa que peça dois números e imprima o maior deles.

n1 = float(input('Informe um numero: '))
n2 = float(input('Informe um segundo numero: '))

if n1 > n2: 
    print('O numero {} é maior que o numero {}'.format(n1, n2))
elif n1 == n2:
    print('ambos os numeros são iguais')
else:
    print('o numero {} é maior que o numero {}'.format(n2, n1))
    