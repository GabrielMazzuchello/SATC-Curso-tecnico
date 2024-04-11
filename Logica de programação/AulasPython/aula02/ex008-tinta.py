#8.	Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e a quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input('informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

area = largura * altura
tinta = area / 2
 
print('A parede tem area de {}M² é será nescessario {} de litros de tinta para pintala.'.format(area, tinta))