while True:
    nome = str(input('Informe o nome do aluno: '))
    senha = str(input('Informe sua senha: '))

    if nome == senha:
        print('Troque de senha pois seu usuario e senha são iguais')
    else:
        print('Seu cadastro foi concluido!')
        break