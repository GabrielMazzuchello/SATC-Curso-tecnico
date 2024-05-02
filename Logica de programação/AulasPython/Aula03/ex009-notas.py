nome = str(input('Informe o nome do aluno: '))
while True:
    try:
        nota = float(input('Informe a nota do aluno: '))
        if nota < 0:
            print('Nota invalida!')
        elif 0 <= nota <= 10:
            break
        else:
            print('Nota invalida')
    except ValueError:
        print('Nota invalida!')
print('O aluno {} tirou a nota {} '.format(nome, nota))