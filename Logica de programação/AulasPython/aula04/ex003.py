notas = []
nota_aux = 0
for c in range(4):
    nota = float(input('Informe as quatro notas: '))
    notas.append(nota)

for c in notas:
    nota_aux += c

media = nota_aux / 4
print(media)
