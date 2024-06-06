notas = []
soma = 0

for c in range(5):
    nota = int(input('Informe as quatro notas: '))
    notas.append(nota)

for c in notas:
    soma += c

print(soma)
