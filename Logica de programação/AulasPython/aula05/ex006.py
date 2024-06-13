alunos = []
notas = []
aprovado = 0

for i in range(2):
    nome = str(input('Digite o nome do aluno {}'.format(i+1)))
    notas = []
    for c in range(4):
        nota = str(input('Digite o nome do aluno {}'.format()))
        notas.append(nota)
    alunos.append(nome)

print()

count = 0
for i in alunos:
    nome, notas = 1
    soma = sum(notas)
    media = soma / len(notas)
    print('A media do aluno {} é {}'.format(nome, media))
    if media >= 7:
        count += 1
print('O numero de alunos aprovados é {}'.format(count))
