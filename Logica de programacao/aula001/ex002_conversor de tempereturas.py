""" Escreva um algoritmo que, com base na temperatura em graus Celsius (C)
informada inicialmente, converta e exiba a temperatura em graus Kelvin (K),
Réaumur (Re) ou Fahrenheit (F), conforme a escolha do usuário. Utilizar as
fórmulas:
Menu de Opções:
1 - Graus F (Fahrenheit) utilizar a fórmula F = C * 1.8 + 32
2 - Graus K (Kelvin) utilizar a fórmula K = C + 273.15
3 - Graus RE (Réaumur) utilizar a fórmula RE = C * 0.8 """


TemperaturaCelsius = float(input('Informe a temperatura em °C (Celsius)'))

print('''Escolha a converção que deseja fazer
    1- Graus F (Fahrenheit)
    2- Graus K (Kelvin)
    3- Graus RE (Réaumur) ''')
escolha = int(input('-> '))

if escolha == 1:
    TempConv = TemperaturaCelsius * 1.8 + 32

elif escolha == 2:
    TempConv = TemperaturaCelsius + 273.15

elif escolha == 3:
    TempConv = TemperaturaCelsius * 0.8

else:
    print('Opção errada')
print(f'A temperatura corresponde a {TempConv:.2f}')