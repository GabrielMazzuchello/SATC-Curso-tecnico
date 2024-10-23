# Aluno: Gabriel Mazzuchello Dal Molin
# Turma: 2137
# 23/10/2024

import mysql.connector
import os

conexao_banco = mysql.connector.connect (
    host="localhost",
    user = "root",
    password = "",
    database = "escola"
)

cursor = conexao_banco.cursor()


def addCurso():
    id = int(input('Informe o id: '))
    nome = input('Informe o nome: ')
    comando_nome = f'SELECT * FROM escola.cursos where nome_curso = "{nome}";'
    cursor.execute(comando_nome)
    dados_nome = cursor.fetchall()

    comando = f'SELECT * FROM escola.cursos where id = {id};'
    cursor.execute(comando)
    dados = cursor.fetchall()
    print(dados_nome)

    if len(dados) > 0 or nome == dados_nome[0][1]:
        os.system('cls')
        print('Erro! esse id ou nome já está sendo utilizado!')

    else:
        nome = input('Informe o nome do curso: ')
        professor = input('Informe do professor: ')
        cargaHoraria = float(input('Informe a carga horaria: '))
        status = input('Informe o status do curso (ativa) ou (inativo): ')

        comando = f'INSERT INTO escola.cursos (id, nome_curso, professor, carga_horaria, status) values({id}, "{nome}", "{professor}", {cargaHoraria}, "{status}");'
        cursor.execute(comando)
        conexao_banco.commit()
        os.system('cls')
        print('cadastro realizado')

def excluir():
    id = int(input('Informe o id: '))

    comando = f'SELECT * FROM escola.cursos where id = {id};'
    cursor.execute(comando)
    dados = cursor.fetchall()

    if len(dados) > 0:
        comando = f'delete from cursos where id = {id};'
        cursor.execute(comando)
        conexao_banco.commit()  
        os.system('cls')
        print("Excluido com sucesso!")   

    else:
        os.system('cls')
        print('Erro! esse id não existe')

def alterar():
    while True:
        id = int(input('Informe o id do curso: '))

        comando = f'SELECT * FROM escola.cursos where id = {id};'
        cursor.execute(comando)
        dados = cursor.fetchall()

        if len(dados) < 0:
            os.system('cls')
            print('Erro! esse curso não existe!')
            break
        
        else:
            os.system('cls')
            print(" 1- alterar nome\n 2- alterar professor\n 3- alterar carga horaria\n 4- status")
            menu2 = int(input('-> '))

            if menu2 == 1:
                os.system('cls')
                novoNome = input('Informe o novo nome: ')
                comando = f'update escola.cursos set nome_curso = "{novoNome}" where id = "{id}";'
                cursor.execute(comando)
                conexao_banco.commit() 
                os.system('cls')
                break
            
            elif menu2 == 2:
                os.system('cls')
                novoProfessor = input('Informe o novo Professor(a): ')
                comando = f'update escola.cursos set professor = "{novoProfessor}" where id = "{id}";'
                cursor.execute(comando)
                conexao_banco.commit() 
                os.system('cls')
                break

            elif menu2 == 3:
                os.system('cls')
                novoCargaHoraria = input('Informe a nova Carga Horaria: ')
                comando = f'update escola.cursos set carga_horaria = "{novoCargaHoraria}" where id = "{id}";'
                cursor.execute(comando)
                conexao_banco.commit()
                os.system('cls')
                break

            elif menu2 == 4:
                os.system('cls')
                novoStatus = input('Informe o novo status (ativa ou inativo): ')
                comando = f'update escola.cursos set status = "{novoStatus}" where id = "{id}";'
                cursor.execute(comando)
                conexao_banco.commit()
                os.system('cls')
                break
            
            else: 
                os.system('cls')
                print('opção errada')

def pesquisar():
    while True:
        os.system('cls')
        print(" 1- pesquisar por professor\n 2- pesquisar por status")
        menu2 = int(input('-> '))

        if menu2 == 1:
            os.system('cls')
            nome = input('Informe o nome do professor: ')
            comando = f'SELECT * FROM escola.cursos where professor = "{nome}";'
            cursor.execute(comando)
            dados = cursor.fetchall()
            exibir(dados)
            break

        elif menu2 == 2:
            os.system('cls')
            status = input('Informe o status (ativa ou inativo): ')
            comando = f'SELECT * FROM escola.cursos where status = "{status}";'
            cursor.execute(comando)
            dados = cursor.fetchall()
            exibir(dados)
            break

def exibir(dados):
    if len(dados) > 0:
        for c in dados:
            print(f'ID: {c[0]} | curso: {c[1]} | professor: {c[2]} | carga horaria: {c[3]} status: {c[4]}')

    else:
        os.system('cls')
        print('Erro dados vazio!')

while True:
    print(" 1- Cadastrar curso\n 2- Alterar curso\n 3- Excluir curso\n 4- Pesquisar\n 5- Sair")
    menu = int(input('->'))

    if menu == 1:
        addCurso()
    
    elif menu == 2:
        alterar()

    elif menu == 3:
        excluir()
    
    elif menu == 4:
        pesquisar()

    elif menu == 5:
        break

    else:
        os.system('cls')
        print('Opção errada!')

