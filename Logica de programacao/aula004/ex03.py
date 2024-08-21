"""Desenvolva um sistema de gerenciamento de tarefas que permita ao usuário adicionar,
visualizar, atualizar e excluir tarefas de uma lista. Cada funcionalidade deve ser implementada
em uma função nomeada específica, e o programa deve chamar essas funções conforme a
necessidade do usuário.
"""
def addTarefa():
    Task = input('Informe sua nova tarefa: ')
    Tasks.append(Task)

def removTarefa():
    TaskRemove = input('Informe a tarefa que deseja remover: ')
    if TaskRemove in Tasks:
        Tasks.remove(TaskRemove)
    else:
        print('A tarefa não foi encontrada.')

def exibirTarefas():
    count = 0
    for c in Tasks:
        count += 1
        print(f'{count}- {c}')

def buscaTarefa():
    try:
        index = int(input('Informe o índice da sua tarefa: ')) - 1
        if 0 <= index < len(Tasks):
            print(f'A tarefa do índice que você digitou é: {Tasks[index]}')
        else:
            print('Índice inválido.')
    except ValueError:
        print('Por favor, informe um número válido.')

Tasks = []
while True:
    print(''' Menu de atividades 
        1- Adicionar uma nova tarefa
        2- Remover uma tarefa existente
        3- Exibir todas as tarefas
        4- Buscar uma tarefa específica
        5- Sair
        ''')
    menu = int(input('-> '))

    match menu:
        case 1:
            addTarefa()
        
        case 2:
            removTarefa()
        
        case 3:
            exibirTarefas()

        case 4:
            buscaTarefa()
        
        case 5:
            break
