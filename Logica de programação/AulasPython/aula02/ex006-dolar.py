#6.	Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#   Considere: US$ 1.00 = R$ 5.41

carteira = float(input('Informe o valor que você tem na carteira: '))

dolar = carteira / 5.41

print('Se você converter terá {} dolares na carteira'.format(dolar))