import mysql.connector
import os 

conexao_banco = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="hotel"
)

cursor = conexao_banco.cursor()

def addProduto():
    id = int(input('Informe o ID: '))
    nome = input('Informe o nome do cliente: ')
    quarto = int(input('Informe o quarto do cliente: '))
    data_entrada = input('Informe a data de entrada: ')
    data_saida = input('Informe a data de saida: ')

    # Verificar se o ID já existe
    comando = 'SELECT COUNT(*) FROM produtos WHERE id = %s'
    cursor.execute(comando, (id,))
    resultado = cursor.fetchone()

    if resultado[0] > 0:
        os.system('cls')
        print('Erro: esse ID já está cadastrado')
    else:
        # Inserir o novo 
        comando = 'INSERT INTO reservas (id, nome, quarto, data_checkin, data_checkout) VALUES (%s, %s, %s, %s, %s)'
        cursor.execute(comando, (id, nome, quarto, data_entrada, data_saida))
        conexao_banco.commit()
        os.system('cls')
        print("Reserva cadastrado com sucesso!")

def excluir():
    id = int(input('Informe o ID da reserva que deseja excluir: '))
    comando = 'DELETE FROM produtos WHERE id = %s'
    cursor.execute(comando, (id,))
    conexao_banco.commit()
    os.system('cls')
    print("Produto excluído com sucesso!")

def pesquisar():
    while True:
        print("""
    === Pesquisar por ===
    1- Nome
    2- Quarto
    3- Sair
    =====================""")
        opcao = int(input('-> '))

        if opcao == 1:
            nome = input('Informe o nome do cliente para buscar: ')
            comando = 'SELECT * FROM reservas WHERE nome = %s'
            cursor.execute(comando, (nome,))
            dados_tabela = cursor.fetchall()
            exibir_resultados(dados_tabela)

        elif opcao == 2:
            cargo = int(input('Informe o cargo do carro para buscar: '))
            comando = 'SELECT * FROM funcionario WHERE cargo = %s'
            cursor.execute(comando, (cargo,))
            dados_tabela = cursor.fetchall()
            exibir_resultados(dados_tabela)

        elif opcao == 3:
            break

        else: 
            print('Opção errada!')

def alterar():
    id = int(input('informe o ID da reserva: '))
    data_entrada = input('Informe a data de entrada: ')
    data_saida = input('Informe a data de saida: ')
    comando = f'UPDATE reservas SET data_checkin, data_checkout = "{data_entrada}", "{data_saida}" where id = {id}'
    cursor.execute(comando)
    conexao_banco.commit()
    os.system('cls')


def exibir_resultados(dados_tabela):
    if dados_tabela:
        for produtos in dados_tabela:
            print(f'ID: {produtos[0]} | Nome: {produtos[1]} | quantidade: {produtos[2]}')
    else:
        print("Nenhum produto encontrado.")

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
        addProduto()

    elif opcao == 2:
        excluir()

    elif opcao == 3:
        exibir_resultados()

    elif opcao == 4:
        alterar()

    elif opcao == 5:
        print('Encerrando o programa...')
        break

    else:
        print('Opção errada!')