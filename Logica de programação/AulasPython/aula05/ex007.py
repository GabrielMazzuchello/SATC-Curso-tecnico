idades = []
alturas = []
altura_total = 0
contador = 0


for c in range(5):
    idade = int(input('Informe sua idade {}: '.format(c+1)))
    altura = float(input('Informe sua altura {}: '.format(c+1)))
    idades.append(idade) 
    alturas.append(altura)
    altura_total += altura
altura_media = altura_total / 5

for idade, altura in zip(idades, alturas):
    if idade > 13 and altura < altura_media:
        contador += 1
print('')
print('a quantidade de alunos é de {}'.format(contador))