import mysql.connector
import os 

conexao_banco = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="carros_1"
)

cursor = conexao_banco.cursor()

def addCarro():
    id = int(input('Informe o ID do carro: '))
    marca = input('Informe a marca do carro: ')
    modelo = input('Informe o modelo do carro: ')
    ano = int(input('Informe o ano do carro: '))  # Garantir que o ano seja um inteiro
    cor = input('Informe a cor do carro: ')

    # Verificar se o ID já existe
    comando = 'SELECT COUNT(*) FROM carros WHERE id = %s'
    cursor.execute(comando, (id,))
    resultado = cursor.fetchone()

    if resultado[0] > 0:
        os.system('cls')
        print('Erro: esse ID já está cadastrado')
    else:
        # Inserir o novo carro
        comando = 'INSERT INTO carros (id, marca, modelo, ano, cor) VALUES (%s, %s, %s, %s, %s)'
        cursor.execute(comando, (id, marca, modelo, ano, cor))
        conexao_banco.commit()
        os.system('cls')
        print("Carro cadastrado com sucesso!")

def excluir():
    id = int(input('Informe o ID do carro que deseja excluir: '))
    comando = 'DELETE FROM carros WHERE id = %s'
    cursor.execute(comando, (id,))
    conexao_banco.commit()
    os.system('cls')
    print("Carro excluído com sucesso!")

def pesquisar():
    while True:
        print("""
    === Pesquisar por ===
    1- Marca
    2- Modelo
    3- Ano
    4- Sair
    =====================""")
        opcao = int(input('-> '))

        if opcao == 1:
            marca = input('Informe a marca do carro para buscar: ')
            comando = 'SELECT * FROM carros WHERE marca = %s'
            cursor.execute(comando, (marca,))
            dados_tabela = cursor.fetchall()
            exibir_resultados(dados_tabela)

        elif opcao == 2:
            modelo = input('Informe o modelo do carro para buscar: ')
            comando = 'SELECT * FROM carros WHERE modelo = %s'
            cursor.execute(comando, (modelo,))
            dados_tabela = cursor.fetchall()
            exibir_resultados(dados_tabela)

        elif opcao == 3:
            ano = int(input('Informe o ano do carro para buscar: '))
            comando = 'SELECT * FROM carros WHERE ano = %s'
            cursor.execute(comando, (ano,))
            dados_tabela = cursor.fetchall()
            exibir_resultados(dados_tabela)

        elif opcao == 4:
            break

        else: 
            print('Opção errada!')

def exibir_resultados(dados_tabela):
    if dados_tabela:
        for carro in dados_tabela:
            print(f'ID: {carro[0]} | Marca: {carro[1]} | Modelo: {carro[2]} | Ano: {carro[3]} | Cor: {carro[4]}')
    else:
        print("Nenhum carro encontrado.")

while True:
    print("""
    ======= Menu =======
    1- Cadastrar
    2- Excluir
    3- Pesquisar
    4- Sair
    ====================""")
    opcao = int(input('-> '))

    if opcao == 1:
        addCarro()

    elif opcao == 2:
        excluir()

    elif opcao == 3:
        pesquisar()

    elif opcao == 4:
        print('Encerrando o programa...')
        break

    else:
        print('Opção errada!')




