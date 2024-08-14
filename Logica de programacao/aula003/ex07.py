""" Faça um programa que receba nome e a média de um aluno.
Crie um dicionário para guardar a situação do aluno (aprovado, reprovado)
No final mostre se o aluno foi aprovado ou reprovado.
"""

Student = {}
Name = input('Informe o nome do aluno: ')
Average = float(input('Informe a media do aluno: '))

Student.update({'Nome': Name})

if Average >= 7:
    Student.update({'Situação': 'Aprovado'})
else:
    Student.update({'situação': 'Reprovado'})

print(Student)