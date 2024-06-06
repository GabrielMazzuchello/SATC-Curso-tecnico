media_lista = []
alunos = int(input('Numero de alunos: '))

for c in range(alunos):
    media = float(input('Informe a media do aluno: '))
    media_lista.append(media)

print('Media dos alunos.')

for c in media_lista:
    print('{}'.format(c))

maior_media = max(media_lista)
menor_media = min(media_lista)

print('A maior média é {} e a menor é {}'.format(maior_media, menor_media))