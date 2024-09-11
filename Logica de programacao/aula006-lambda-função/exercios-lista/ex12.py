"""Imagine que você está trabalhando em um sistema de e-commerce que aplica descontos
progressivos com base na quantidade de produtos comprados. Crie uma função que receba uma
lista de preços e um valor de desconto percentual. A função deve usar map() e lambda para
aplicar o desconto a cada item e retornar uma nova lista com os preços atualizados.
Dica: Use uma função def para aplicar o desconto e utilize map() dentro dela."""

"""def desconto():
    if len(produtos) >= 5:
        desconto = list(map(lambda x : x-(x*0.10)), produtos)
    elif len(produtos) >= 10:
        desconto = list(map(lambda x : x-(x*0.20)), produtos)
    elif len(produtos) >= 15:
        desconto = list(map(lambda x : x-(x*0.35)), produtos)
    return desconto"""


produtos = []
while True: 
    produto = float(input('Informe o valor do produto: '))
    produtos.append(produto)

    if len(produtos) == 5:
        print(list(map(lambda x : x-(x*0.35)), produtos))
    elif len(produtos) == 10:
        print(list(map(lambda x : x-(x*0.35)), produtos))
    elif len(produtos) == 15:
        print(list(map(lambda x : x-(x*0.35)), produtos))
    

    



