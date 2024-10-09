import mysql.connector
import os 

conexao_banco = mysql.connector.connect (
    host = "127.0.0.1",
    user= "root",
    password = "",
    database = "carros_1"
)

cursor = conexao_banco.cursor()

def addCarro():
    marca = input('Informe a marca do carro: ')
    modelo = input('Informe o modelo do carro: ')
    ano = int(input('informe o ano do carro: '))
    cor = input('Informe a cor do carro: ')

    comando = 'SELECT CIUNT(*) FROM carros Where marca %s AND modelo = %s ano = %s'
    cursor.execute(comando, (marca, modelo, ano))
    resultado = cursor.fetchone()
    

    if resultado[0] > 0:
        print('Erro: esse veiculo já está cadastrado')

    else:
        comando = (f'INSERT INTO carros (marca, modelo, ano, cor)   VALUES ("{marca}", {modelo}, {ano}, "{cor}")')
        cursor.execute(comando)
        conexao_banco.commit()
        os.system('cls')

def excluir():
    id = int(input('informe o ID do carro que deseja excluir: '))
    comando = f'DELETE FROM carros WHERE id = {id};'
    cursor.execute(comando)
    conexao_banco.commit()
    os.system('cls')



while True:
    print("""
    ======= Menu =======
    1- cadastrar
    2- excluir
    3- pesquisar
    4- sair
    ====================""")
    opcao = int(input(''))

    if opcao == 1:
        addCarro()

    elif opcao == 2:
        excluir()

    elif opcao == 4:
        print('Encerrando o programa...')
        break

