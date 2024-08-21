"""Desenvolva uma calculadora que permita ao usuário escolher entre as operações de adição,
subtração, multiplicação e divisão. Para cada operação, crie uma função nomeada que realize o
cálculo correspondente. O programa deve chamar a função apropriada com base na escolha do
usuário."""

import math

def adicao():
    resultado = numero1 + numero2
    return resultado


def subtracao():
    resultado = numero1 - numero2
    return resultado


def multiplicacao():
    resultado = numero1 * numero2
    return resultado


def divisao():
    resultado = numero1 / numero2
    return resultado



while True:
    print(f'''    |{' Operação ':=^30}|
    |       [+] Adição             |
    |       [-] Subtração          |
    |       [*] Multiplicação      |
    |       [/] Divizão            |
    |       [S] Sair               |
    |{'=' * 30}|''')
    operacao = str(input()).strip()

    if operacao.upper() == 'S':
        print('{: ^30}'.format('Fim do Programa'))
        break

    else:  # verificado a operação
        if (operacao == '+') or (operacao == '-') or (operacao == '*') or (operacao == '/') or (operacao == '**'):
            try:  # tratamento de erro
                numero1 = float(input('Informe o 1° numero: '))
                numero2 = float(input('Informe o 2° numero: '))

                if operacao == '+':  # chamando as funçoes
                    print(adicao())
                elif operacao == '-':
                    print(subtracao())
                elif operacao == '*':
                    print(multiplicacao())
                elif operacao == '/':
                    print(divisao())
            except ValueError:
                print('{: ^36}'.format('Somente numeros'))
        else:
            print('{: ^36}'.format('Operação invalida'))