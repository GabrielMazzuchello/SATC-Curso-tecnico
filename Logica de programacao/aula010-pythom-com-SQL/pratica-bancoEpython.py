import mysql.connector
import os 

conexao_banco = mysql.connector.connect (
    host = "127.0.0.1",
    user= "root",
    password = "",
    database = "listatelefone"
)

cursor = conexao_banco.cursor()


while True:
    print('1- adicionar \n 2- atualizar \n 3- remover \n 4- consultar \n 5- sair')
    op = int(input(''))

    if op == 1:
        nome = input('Informe o nome: ')
        telefone = int(input('informe o telefone: '))
        cidade = input('infoeme a cidade: ')
        CPF = int(input('Informe o CPF: '))

        comando = (f'INSERT INTO cadastrocliente (nome, telefone, cidade, CPF)   VALUES ("{nome}", {telefone}, {CPF}, "{cidade}")')
        cursor.execute(comando)
        conexao_banco.commit()
        os.system('cls')

    elif op == 2:
        while True:
            
            nome = input('Informe o nome do produto')
            comando = f'UPDATE produtos SET nome = {nome} where id_produtos = {id}'
            cursor.execute(comando)
            conexao_banco.commit()


    elif op == 3:
        codigo = int(input('Informe o codigo para excluir: '))
        comando = f'DELETE FROM cadastrocliente WHERE codigo = {codigo};'
        cursor.execute(comando)
        conexao_banco.commit()
        os.system('cls')

    elif op == 4:
        codigo = int(input('Informe o codigo para consultar: '))
        comando = f'SELECT * from cadastrocliente'
        cursor.execute(comando)
        dados_tabela = cursor.fetchall()
        print(f'ID: {dados_tabela[codigo-1][0]} nome: {dados_tabela[codigo-1][1]} telefone: {dados_tabela[codigo-1][2]} CPF: {dados_tabela[codigo-1][3]} cidade: {dados_tabela[codigo-1][4]}')
        os.system('cls')

    elif op == 5:
        os.system('cls')
        print('fim do programa!')
        break
