""" Crie um dicionário pessoa e coloque nele os dados fornecidos pelo usuário: nome, idade, telefone, endereço. Imprima 
todos os itens do dicionário no formato chave : valor
"""
pessoas = {}

nome = input('Informe seu nome: ')
pessoas.update({'Nome': nome})

Idade = input('Informe seu Idade: ')
pessoas.update({'Idade': Idade})

Telefone = input('Informe seu telefone: ')
pessoas.update({'Telefone': Telefone})

Endereco = input('Informe seu endereço: ')
pessoas.update({'Endereco': Endereco})

for chave, valor in pessoas.items():
    print(f'{chave}: {valor}')