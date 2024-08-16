# Crie um dicionário pessoa e coloque nele seus dados: nome, idade, telefone, endereço. Usando o dicionário pessoa criado anteriormente, imprima seu nome.

pessoas = {}

nome = input('Informe seu nome: ')
pessoas.update({'Nome': nome})

Idade = input('Informe seu Idade: ')
pessoas.update({'Idade': Idade})

Telefone = input('Informe seu telefone: ')
pessoas.update({'Telefone': Telefone})

Endereco = input('Informe seu endereço: ')
pessoas.update({'Endereco': Endereco})

print(pessoas(pessoas['nome']))
