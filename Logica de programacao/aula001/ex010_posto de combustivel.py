"""10) Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
a. até 20 litros, desconto de 3% por litro
b. acima de 20 litros, desconto de 5% por litro
Gasolina:
c. até 20 litros, desconto de 4% por litro
d. acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A - álcool, G - gasolina), calcule e imprima o valor a ser
pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 5,65 o preço do litro
do álcool é R$ 4,22."""

Liters = float(input('Informe a quantidade de litros de combustivel que foi abastecido: '))
print('''Tipo de combustivel
      A- álcool
      G- gasolina
''')
menu = input('-> ').upper().strip()[0]

if menu == 'A':
    if Liters <= 20:
        price = Liters * 4.09
    
    elif Liters > 20:
        price = Liters * 4.01

elif menu == 'G':
    if Liters <= 20:
        price = Liters * 5.42
    
    elif Liters > 20:
        price = Liters * 5.31

print(f'O total a pagar foi de {price}')