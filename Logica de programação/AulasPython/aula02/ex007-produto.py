#7.	Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto e com 15% de aumento

preco = float(input('Informe o preço do produto: '))

almento = preco * 1.15
desconto = preco * 0.95

print('o preço do produto com disconto ficou de {} e o preço do produto com almento ficou {}.'.format(desconto, almento))