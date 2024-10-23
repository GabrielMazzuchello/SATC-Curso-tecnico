# Aluno: Gabriel Mazzuchello Dal Molin
# Turma: 2137
# 23/10/2024

import mysql.connector
import os

conexao_banco = mysql.connector.connect (
    host="localhost",
    user = "root",
    password = "",
    database = "imobiliaria"
)

cursor = conexao_banco.cursor() # conexão do banco 



def addImovel(): # função de adicionar imovel
    id = int(input('Informe o id: '))
    endereco = input('Informe o nome: ')
    comando_endereco = f'SELECT * FROM imobiliaria.imoveis where endereco = "{endereco}";' # comando sql para  verificar o endereço
    cursor.execute(comando_endereco) # comando para execultar o comando no banco de dados
    dados_nome = cursor.fetchall() # salva os item que retornou do banco em uma variavel (tupla)

    comando = f'SELECT * FROM imobiliaria.imoveis where id = {id};' # comando sql para  verificar o id
    cursor.execute(comando)
    dados = cursor.fetchall()

    if len(dados) > 0 or endereco == dados_nome[0][1]:
        os.system('cls') # todos os  os.system('cls')  servem para limpar a tela
        print('Erro! esse id ou endereço já está sendo utilizado!')

    else:
        endereco = input('Informe o endereço: ')
        tipo = input('Informe o tipo do imovel: ')
        preco = float(input('Informe o valor do imovel: '))
        status = input('Informe o status do imovel (à venda) ou (vendido): ')

        comando = f'INSERT INTO imobiliaria.imoveis (id, endereco, tipo, preco, status) values({id}, "{endereco}", "{tipo}", {preco}, "{status}");'
        cursor.execute(comando)
        conexao_banco.commit()
        print('cadastro realizado')

def excluir(): # função de excluir imovel
    id = int(input('Informe o id: '))

    comando = f'SELECT * FROM imobiliaria.imoveis where id = {id};' 
    cursor.execute(comando)
    dados = cursor.fetchall()

    if len(dados) > 0:
        comando = f'delete from imoveis where id = {id};' # deleta os itens com o id digitado
        cursor.execute(comando)
        conexao_banco.commit()  
        os.system('cls') 
        print("Excluido com sucesso!")   

    else:
        os.system('cls')
        print('Erro! esse id não existe') # tratamento de erro para caso o id informado não exista

def alterarStatus(): # função para alterar o status do imovel
    id = int(input('Informe o id: '))

    comando = f'SELECT * FROM imobiliaria.imoveis where id = {id};'
    cursor.execute(comando)
    dados = cursor.fetchall()

    if len(dados) <= 0:
        os.system('cls')
        print('Erro! esse id não existe!')

    else: 
        novoStatus = input("Informe o novo status do imovel: ")
        comando = f'update imobiliaria.imoveis set status = "{novoStatus}" where id = "{id}";'
        cursor.execute(comando)
        conexao_banco.commit()
    

def pesquisar(): # função para pesquisar / buscar 
    while True: # repetição da busca 
        os.system('cls')
        print(" 1- pesquisar por tipo\n 2- pesquisar por faixa de preço")
        menu2 = int(input('-> '))

        if menu2 == 1:
            os.system('cls')
            opcao = input('escolha pesquisar por casa ou apartamento: ') # pesquisa pelo tipo
            comando = f'SELECT * FROM imobiliaria.imoveis where tipo = "{opcao}";'
            cursor.execute(comando)
            dados = cursor.fetchall()
            exibir(dados)
            break

        elif menu2 == 2:
            os.system('cls')
            faxainicio = float(input('informe a faixa do inicio: ')) # pesquisa pela faixa
            faixafinal = float(input('informe a faixa do final: '))
            comando = f'SELECT * FROM imobiliaria.imoveis where preco >= {faxainicio} and preco <= {faixafinal};'
            cursor.execute(comando)
            dados = cursor.fetchall()
            exibir(dados)
            break


def exibir(dados): # função que está dentro da pesquisar que serve apenas para mostrar os dados ao usuario
    if len(dados) > 0:
        for c in dados:
            print(f'ID: {c[0]} | endereço: {c[1]} | tipo: {c[2]} | preço: {c[3]} status: {c[4]}')

    else:
        os.system('cls')
        print('Erro dados vazio!')

while True: # repetição principal
    print(" 1- Cadastrar imovel\n 2- Excluir imovel\n 3- Alterar status\n 4- Pesquisar\n 5- Sair") # menu
    menu = int(input('->')) # recebe o valor do usuario

    if menu == 1:
        addImovel()

    elif menu == 2:
        excluir() 

    elif menu == 3:
        alterarStatus()

    elif menu == 4:
        pesquisar()

    elif menu == 5:
        break


