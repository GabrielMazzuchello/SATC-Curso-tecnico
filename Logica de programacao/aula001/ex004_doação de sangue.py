"""O HEMOSC de uma cidade deseja controlar as doações de sangue de seus
pacientes. Faça um algoritmo que receba como entrada os dados do paciente:
nome do paciente, idade e peso. Após verifique se o doador se encaixa nas
categorias de doação e mostre uma mensagem:

a. Pessoas de 0 a 15 anos não podem ser doadores estarem abaixo da idade
permitida.
b. Pessoas de 16 e 17 anos e que estejam pesando mais de 55 kg, podem ser
doadores com autorização dos pais ou responsáveis.
c. Pessoas de 18 a 69 e que estejam pesando mais de 60 kg, podem ser
doadores.
d. Pessoas acima de 69 anos não podem ser doadores por estarem acima da
idade permitida"""

name = input('Informe seu nome: ')
age = int(input('Informe sua iadde: '))
Weight = float(input('Informe seu peso: '))

if 0 <= age >= 15:
    print(f'Infelismente {name} você não pode doar sangue pois possui menos de 16 anos')

elif 16 <= age >= 17 and Weight < 55:
    print(f'Você não pode doar pois seu peso é baixo')

elif 18 <= age >= 69 and Weight < 60:
    print('Você pode doar sangue')

elif age > 69:
    print('Voce não pode doar pois está em uma idade avançada')

