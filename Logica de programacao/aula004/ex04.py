"""Crie um aplicativo de agenda de contatos que permita ao usuário adicionar, visualizar, editar e
excluir contatos. Cada operação deve ser realizada por uma função nomeada separada, e o
programa deve gerenciar os contatos utilizando essas funções."""


def addContato():
    novoContato = {}
    nome = input('Informe o nome: ')
    numero = int(input('Informe o numero: '))
    novoContato['nome'] = nome
    novoContato['telefone'] = numero
    Contatos.append(novoContato)

def todosContatos():
    for contato in Contatos:
        print(f'Nome: {contato['nome']} Telefone: {contato['telefone']}')

    
def excluirContato():
    count = 0
    

def buscaTarefa():
    try:
        index = int(input('Informe o índice da sua tarefa: ')) - 1
        if 0 <= index < len(Contatos):
            print(f'A tarefa do índice que você digitou é: {Contatos[index]}')
        else:
            print('Índice inválido.')
    except ValueError:
        print('Por favor, informe um número válido.')

Contatos = []
while True:
    print(''' Menu de atividades 
        1- Adicionar uma novo contato
        2- Excluir um contato existente
        3- visualizar todas as contatos
        4- Buscar uma tarefa específica
        5- Sair
        ''')
    menu = int(input('-> '))

    match menu:
        case 1:
            addContato()
        
        case 2:
            todosContatos()
        
        case 3:
            todosContatos()

        case 4:
            buscaTarefa()
        
        case 5:
            break
