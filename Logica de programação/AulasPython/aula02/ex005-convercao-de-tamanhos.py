#5.	Faça um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

metros = float(input('Informe um valor em metros: '))

centimetros = metros * 100
milimetros = centimetros * 10

print('o valor {} em metros corresponde a {} em centrimetros e a {} em milimetros'.format(metros, centimetros, milimetros))