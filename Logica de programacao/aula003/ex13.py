""" 13)	Utilizando a linguagem PYTHON com dicionários e estruturas de repetição, criar um programa que contenha um MENU de opções, para gerenciar os cargos e funcionários de uma Empresa, conforme as solicitações abaixo.  Exemplo: 
MENU de Opções
C – Cadastrar 
A – Alterar 
E - Excluir
P – Pesquisar
S – Sair
               
Para cada opção do Menu, devemos construir:
a)	Se usuário escolher opção C – Cadastrar Cargos e Funcionários, devemos inserir os elementos no dicionário com o nome funcionário e o seu cargo. Exemplo: dic = { “Cris” : “Gerente” }
b)	Se usuário escolher opção A – Alterar, devemos alterar os elementos do dicionario. Perguntar ao usuário qual informação ele deseja alterar (Cargo ou Funcionário) e verificar se a informação já foi cadastrada. Exibir mensagens de verificação.
c)	Se usuário escolher opção E – Excluir, devemos excluir os elementos do dicionário. Perguntar ao usuário qual informação ele deseja excluir (Cargo ou Funcionário) e verificar se a informação já foi cadastrada. Exibir mensagens de verificação.
d)	Se usuário escolher opção P – Pesquisar, devemos mostrar os elementos já cadastrados nas listas (Cargos e Funcionários). Mostrar a lista completa, mostrar a lista em ordem alfabética e o total de funcionarios cadastrados.
e)    Se usuário escolher opção S – Sair, encerrar o programa com uma mensagem.
 """
empresa = {}
count = 0
while True:
    print('='*10, 'CADASTRO EMPRESA', '='*10)
    menu = input('Digite sua opção:'
                   '\nC-Cadastrar'
                   '\nA-Alterar'
                   '\nE-Excluir'
                   '\nP-Pesquisar'
                   '\nS-sair\n').upper().strip()

    if menu == 'C':
        nome = input('Digite o nome do funcionário: ')
        cargo= input('digite o cargo do funcionário: ')
        count += 1
        empresa.update({count:[nome,cargo]})
        print(empresa)
        
    elif menu == 'A':
        verifica_funcionario = int(input('Digite o codigo do funcionário que deseja alterar: '))
        if verifica_funcionario in empresa:
            alterar = input('digite F para alterar o nome do funcionário ou C para alterar o cargo: ').upper().strip()
            if alterar == 'F':
                novo_nome = input('digite o novo nome: ')
                empresa[verifica_funcionario][0] = novo_nome
                print(empresa)
            
            elif alterar == 'C':
                novo_cargo = input('digite o novo cargo: ')
                empresa[verifica_funcionario][1] = novo_cargo
                print(empresa)
            else:
                print('Você não digitou uma opção válida')
        else:
            print('Codígo de funcionário inexistente')

    elif menu == 'E':
        verifica_funcionario = int(input('Digite o codigo do funcionário que deseja alterar: '))
        if verifica_funcionario in empresa:
            del empresa[verifica_funcionario]
            print(empresa)
        else:
            print('Codígo de funcionário inexistente')

    elif menu == 'P':
        verifica_funcionario = int(input('Digite o codigo do funcionário que deseja alterar: '))
        if verifica_funcionario in empresa:
            print(empresa[verifica_funcionario])
        else:
            print('Codígo de funcionário inexistente')
    
    elif menu == 'S':
        print('='*40)
        print('Obrigado por usar nosso sistema.\nAté logo.')
        break

    else:
        print('Nã foi possível encontrar a opção que desejou, escolha uma das opções abaixo: ')
    
             