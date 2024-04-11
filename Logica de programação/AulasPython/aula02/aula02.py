
materia = str(input('Qual é a materia que deseja informar as notas(Portugues, Fizica)')).lower()


if materia == "portugues":
    nteoria = float(input('Digite sua nota da teoria: '))
    npratica = float(input('Digite sua nota da pratica: '))

    notatotal = nteoria + npratica

    if (nteoria >= 0 and nteoria <= 5) and (npratica >=0 and npratica <= 5):
        if notatotal > 10 or notatotal < 0:
            print('Nota invalida')
        elif notatotal >= 6:
            print('aprovado')
        elif notatotal < 6 and notatotal >= 4.5: 
            print('recuperação')
        else:
            print('Reprovado')
    elif nteoria < 0 or npratica < 0:
        print('Notas invalidas, ultrapassãm o valor minimo')

elif materia == "fizica":
    nteoria = float(input('Digite sua nota da teoria: '))
    npratica = float(input('Digite sua nota da pratica: '))

    notatotal = nteoria + npratica

    if (nteoria >= 0 and nteoria <= 4) and (npratica >=0 and npratica <= 6):
        if notatotal > 10 or notatotal < 0:
            print('Nota invalida')
        elif notatotal >= 6:
            print('aprovado')
        elif notatotal < 6 and notatotal >= 4.5: 
            print('recuperação')
        else:
            print('Reprovado')
    elif nteoria < 0 or npratica < 0:
        print('Notas invalidas, ultrapassãm o valor minimo')

else:
    print('Matéria invalida!!')
    


















