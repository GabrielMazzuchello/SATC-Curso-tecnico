""" Crie um programa que cadastre informações de várias pessoas (nome, idade e cpf) e as adicione em um dicionário. 
Mostre os nomes de todas as pessoas menores de 18 anos."""

Informacoes = []

for c in range(3):
    usuario = {}

    print('-=-' * 10)
    Cpf = int(input('Informe seu cpf: '))
    Nome = input('Informe seu nome: ')
    Idade = int(input('informe sua idade: '))

    usuario.update({'CPF': Cpf})
    usuario.update({'Nome': Nome})
    usuario.update({'Idade': Idade})

    Informacoes.append(usuario)

print('-=-' * 10)
for Value in Informacoes:
    if Value['Idade'] >= 18:
        print(Value['Nome'])