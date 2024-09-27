"""Imagine que você está trabalhando em um sistema de e-commerce que aplica descontos
progressivos com base na quantidade de produtos comprados. Crie uma função que receba uma
lista de preços e um valor de desconto percentual. A função deve usar map() e lambda para
aplicar o desconto a cada item e retornar uma nova lista com os preços atualizados.
Dica: Use uma função def para aplicar o desconto e utilize map() dentro dela."""

def aplica_desconto(produtos, percentual_desconto):
    # Aplica o desconto a cada produto usando map e lambda
    return list(map(lambda x: x - (x * percentual_desconto), produtos))

produtos = []

while True: 
    produto = float(input('Informe o valor do produto: '))
    produtos.append(produto)

# Verifica a quantidade de produtos e aplica o desconto correto
    if len(produtos) >= 15:
        # Desconto de 35% para 15 ou mais produtos
        print(aplica_desconto(produtos, 0.35))
    elif len(produtos) >= 10:
        # Desconto de 20% para 10 ou mais produtos
        print(aplica_desconto(produtos, 0.20))
    elif len(produtos) >= 5:
        # Desconto de 10% para 5 ou mais produtos
        print(aplica_desconto(produtos, 0.10))
