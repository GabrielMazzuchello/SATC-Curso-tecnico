#4.	Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo.

n1 = float(input('Informe um numero positivo ou negativo: '))

if n1 > 0:
    print('O numero informado é possitivo')
elif n1 < 0:
    print('O numero informado é negativo')