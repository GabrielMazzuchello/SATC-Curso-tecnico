"""A Secretaria de Educação do Município deseja realizar um levantamento com seus
alunos, definido por nível de ensino. Elabore um algoritmo que leia o nome e idade
do aluno e mostre em que nível escolar ele se encontra, de acordo com a tabela
abaixo:
Idade Nível Escolar
de 0 a 2 anos Berçário
de 3 a 6 anos Educação Infantil
de 7 a 10 anos Fundamental Nível I
de 11 a 15 anos Fundamental Nível II
de 16 a 18 anos Ensino Médio
"""

name = input('Informe o nome do aluno: ')
age = int(input('Informe a idade do aluno: '))

if 0 <= age <= 2:
    print(f'O aluno {name} esta no berçário')
elif 3 <= age <= 6:
    print(f'O aluno {name} esta no Educação Infantil')
elif 7 <= age <= 10:
    print(f'O aluno {name} esta no Fundamental Nível I')
elif 11 <= age <= 15:
    print(f'O aluno {name} esta no Fundamental Nível II')
elif 16 <= age <= 18:
    print(f'O aluno {name} esta no Ensino Médio')
elif age > 18:
    print(f'{name} não é um aluno')