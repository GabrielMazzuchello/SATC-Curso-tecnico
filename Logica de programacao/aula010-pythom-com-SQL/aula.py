import mysql.connector

conexao_banco = mysql.connector.connect (
    host = "127.0.0.1",
    user= "root",
    password = "",
    database = "mercearia"
)

cursor = conexao_banco.cursor()

"""#CRUD
# Create, Read, Update, Delete

#create

nomeProduto = input('informe o nome no produto: ')
valorProduto = float(input('informe o valor do produto: '))

comando = (f'INSERT INTO produtos (nome, valor_produto)   VALUES ("{nomeProduto}", {valorProduto})')
cursor.execute(comando)
conexao_banco.commit()"""

# update
"""valor_novo = 10
id = int(input('informe o id: '))
# comando = f'UPDATE produtos SET valor_produto = {valor_novo} where id_produtos = {id}'

nome = input('Informe o nome do produto')
comando = f'UPDATE produtos SET nome = {nome} where id_produtos = {id}'
cursor.execute(comando)
conexao_banco.commit()"""


# delete
"""id = int(input('informe o id para deletar o produto: '))
comando = f'DELETE FROM produtos WHERE id_produtos = {id};'
cursor.execute(comando)
conexao_banco.commit()"""

# read

comando = 'SELECT * from produtos'
cursor.execute(comando)
dados_tabela = cursor.fetchall()

for i in dados_tabela:
    print(f'ID: {i[0]} nome: {i[1]} valor: {i[2]}')

