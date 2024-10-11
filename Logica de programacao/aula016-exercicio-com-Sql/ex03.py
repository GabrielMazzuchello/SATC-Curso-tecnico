import mysql.connector
import os 

conexao_banco = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="loja"
)

cursor = conexao_banco.cursor()

def addProduto():
    id = int(input('Informe o ID do produto: '))
    nome = input('Informe o nome do produto: ')
    quantidade = int(input('Informe a quantidade do produto: '))

    # Verificar se o ID já existe
    comando = 'SELECT COUNT(*) FROM produtos WHERE id = %s'
    cursor.execute(comando, (id,))
    resultado = cursor.fetchone()

    if resultado[0] > 0:
        os.system('cls')
        print('Erro: esse ID já está cadastrado')
    else:
        # Inserir o novo 
        comando = 'INSERT INTO produtos (id, nome, quantidade) VALUES (%s, %s, %s)'
        cursor.execute(comando, (id, nome, quantidade))
        conexao_banco.commit()
        os.system('cls')
        print("Produto cadastrado com sucesso!")

def excluir():
    id = int(input('Informe o ID do produto que deseja excluir: '))
    comando = 'DELETE FROM produtos WHERE id = %s'
    cursor.execute(comando, (id,))
    conexao_banco.commit()
    os.system('cls')
    print("Produto excluído com sucesso!")

def pesquisar():
    comando = 'SELECT * FROM produtos;'
    cursor.execute(comando)
    dados_tabela = cursor.fetchall()
    exibir_resultados(dados_tabela)

def alterar():
    id = int(input('informe o Id do produto: '))
    quantidade = input('Informe a nova quantidade do produto: ')
    comando = f'UPDATE produtos SET quantidade = "{quantidade}" where id = {id}'
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