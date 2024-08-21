"""Crie um programa que exiba um menu de opções para calcular a área de um círculo, um
retângulo ou um triângulo. Cada cálculo deve ser realizado por uma função nomeada distinta. A
função deve receber os parâmetros necessários (como raio, base, altura, etc.) e retornar a área
calculada"""
import math
def areaCirculo():
    raio = float(input('Informe o raio da circunferencia: '))
    area = 3.14 * raio ** 2
    print(f'A area do circulo é de {area}')

def areaRetangulo():
    base = float(input('Informe a base do retângulo: '))
    altura = float(input('Informe a altura do retângulo'))
    area = base * altura
    print(f'A área do retângulo é {area}')

def areaTriangulo():
    base = float(input('Informe o comprimento da base do triangulo (m): '))
    altura = float(input('Informe a altura do triangulo (m): '))
    area = base * altura / 2
    print(f'A área do triangulo é {area} m')


while True:
    print("""1 - Área do círculo
2 - Área do retângulo
3 - Área do triângulo""")
    menu = int(input('-> '))

    if menu == 1:
        areaCirculo()
    elif menu == 2:
        areaRetangulo()
    elif menu == 3:
        areaTriangulo()

