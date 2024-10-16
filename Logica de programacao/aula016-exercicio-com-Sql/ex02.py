import mysql.connector
import os 

conexao_banco = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="gerenciamento_funcionarios"
)

cursor = conexao_banco.cursor()

def addFuncionario():
    id = int(input('Informe o ID do funcionario: '))
    
    # Verificar se o ID já existe
    comando = 'SELECT COUNT(*) FROM funcionario WHERE id = %s'
    cursor.execute(comando, (id,))
    resultado = cursor.fetchone()

    if resultado[0] > 0:
        os.system('cls')
        print('Erro: esse ID já está cadastrado')
    else:
        # Inserir o novo carro
        nome = input('Informe o nome do funcionario: ')
        cargo = input('Informe o cargo do funcionario: ')
        comando = 'INSERT INTO funcionario (id, nome, cargo) VALUES (%s, %s, %s)'
        cursor.execute(comando, (id, nome, cargo))
        conexao_banco.commit()
        os.system('cls')
        print("Funcionario cadastrado com sucesso!")

def excluir():
    id = int(input('Informe o ID do funcionario que deseja excluir: '))
    comando = 'DELETE FROM funcionario WHERE id = %s'
    cursor.execute(comando, (id,))
    conexao_banco.commit()
    os.system('cls')
    print("Funcionario excluído com sucesso!")

def pesquisar():
    while True:
        print("""
    === Pesquisar por ===
    1- Nome
    2- Cargo
    3- Sair
    =====================""")
        opcao = int(input('-> '))

        if opcao == 1:
            nome = input('Informe o nome do funcionario para buscar: ')
            comando = 'SELECT * FROM funcionario WHERE nome = %s'
            cursor.execute(comando, (nome,))
            dados_tabela = cursor.fetchall()
            exibir_resultados(dados_tabela)

        elif opcao == 2:
            cargo = input('Informe o cargo do carro para buscar: ')
            comando = 'SELECT * FROM funcionario WHERE cargo = %s'
            cursor.execute(comando, (cargo,))
            dados_tabela = cursor.fetchall()
            exibir_resultados(dados_tabela)

        elif opcao == 3:
            break

        else: 
            print('Opção errada!')

def alterar():
    id = int(input('informe o Id do funcionario: '))
    cargo = input('Informe o novo cargo do funcionario: ')
    comando = f'UPDATE funcionario SET cargo = "{cargo}" where id = {id}'
    cursor.execute(comando)
    conexao_banco.commit()
    os.system('cls')


def exibir_resultados(dados_tabela):
    if dados_tabela:
        for funcionario in dados_tabela:
            print(f'ID: {funcionario[0]} | Nome: {funcionario[1]} | Cargo: {funcionario[2]}')
    else:
        print("Nenhum carro encontrado.")

while True:
    print("""
    ======= Menu =======
    1- Cadastrar
    2- Excluir
    3- Pesquisar
    4- Alterar
    5- Sair
    ====================""")
    opcao = int(input('-> '))

    if opcao == 1:
        addFuncionario()

    elif opcao == 2:
        excluir()

    elif opcao == 3:
        pesquisar()

    elif opcao == 4:
        alterar()

    elif opcao == 5:
        print('Encerrando o programa...')
        break

    else:
        print('Opção errada!')




