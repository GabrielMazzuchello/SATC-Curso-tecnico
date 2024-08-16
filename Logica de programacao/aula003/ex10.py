"""Crie um dicionário que será uma agenda e coloque nele os seguintes dados: cpf, nome, idade, telefone. O programa 
deve ler um número 5 usuários, criar a agenda e imprimir todos os itens do dicionário formatos."""

agenda = []

for c in range(3):
    usuario = {}

    Cpf = int(input('Informe seu cpf: '))
    Nome = input('Informe seu nome: ')
    Idade = int(input('informe sua idade: '))
    Telefone = int(input('informe seu telefone: '))

    usuario.update({'CPF': Cpf})
    usuario.update({'Nome': Nome})
    usuario.update({'Idade': Idade})
    usuario.update({'Telefone': Telefone})

    agenda.append(usuario)

for c in agenda:
    print(c)