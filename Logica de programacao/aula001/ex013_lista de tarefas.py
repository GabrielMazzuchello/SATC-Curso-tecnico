"""13) Uma empresa de desenvolvimento de software quer criar um aplicativo para ajudar as
pessoas a gerenciarem suas listas de tarefas diárias. Você foi contratado para
desenvolver um protótipo desse aplicativo em Python. O programa deve apresentar um
menu interativo que permita aos usuários realizarem várias operações na lista de
tarefas.
As operações disponíveis no menu devem incluir:
a. Adicionar uma nova tarefa: O usuário deve poder adicionar uma nova tarefa
à lista.
b. Remover uma tarefa existente: O usuário deve poder remover uma tarefa
específica da lista.
c. Exibir todas as tarefas: O programa deve listar todas as tarefas atualmente
na lista uma embaixo da outra.
d. Buscar uma tarefa específica: O usuário deve poder procurar uma tarefa
específica na lista.
e. Sair do programa: O usuário deve poder sair do programa quando desejar."""

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
            Task = input('Informe sua nova tarefa: ')
            Tasks.append(Task)
        
        case 2:
            TaskRemove = input('Informe a tarefa que deseja remover: ')
            if TaskRemove in Tasks:
                Tasks.remove(TaskRemove)
            else:
                print('A tarefa não foi encontrada.')
        
        case 3:
            count = 0
            for c in Tasks:
                count += 1
                print(f'{count}- {c}')
        case 4:
            try:
                index = int(input('Informe o índice da sua tarefa: ')) - 1
                if 0 <= index < len(Tasks):
                    print(f'A tarefa do índice que você digitou é: {Tasks[index]}')
                else:
                    print('Índice inválido.')
            except ValueError:
                print('Por favor, informe um número válido.')
        
        case 5:
            break
