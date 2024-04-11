#9.	Construir um programa que leia nome e valor em dinheiro (reais) de uma pessoa. Calcule e retorne uma mensagem com o valor convertido para Dólar e calcule e retorne uma mensagem com o valor convertido para Euros.
import time
nome = str(input('Informe su nome: '))
carteira = float(input('Informe o seu saldo para convertermos: '))

dolar = carteira * 5,1
euro = carteira * 5,46

print('Convertendo...')
time.sleep(3)

print('A converção ficou pra dolar foram {} e para euros foram {}'.format(dolar, euro))
