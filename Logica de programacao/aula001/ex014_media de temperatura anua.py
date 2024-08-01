"""
14) Faça um programa que receba a temperatura média de cada mês do ano e
armazene-as em uma lista. Após isto:
a. calcule a média anual das temperaturas;
b. mostre todas as temperaturas acima da média anual, e em que mês elas
ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""

temperaturas = []
meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]

for i in range(12):
    while True:
        try:
            temp = float(input(f'Informe a temperatura média de {meses[i]}: '))
            temperaturas.append(temp)
            break
        except ValueError:
            print('Informe um valor numérico válido.')
    
media_anual = sum(temperaturas) / len(temperaturas)
print(f'\nA média anual das temperaturas é: {media_anual:.2f}°C')

print("\nTemperaturas acima da média anual:")
for i, temp in enumerate(temperaturas):
    if temp > media_anual:
        print(f'{meses[i]}: {temp:.2f}°C')