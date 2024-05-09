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
    print('==============================')
    print('=        1- Adição           =')
    print('=        2- Subtração        =')
    print('=        3- Multiplicação    =')
    print('=        4- Divisão          =')
    print('=        5- Sair do programa =')
    print('==============================')
    try:
        menu = int(input(''))
        if menu == 5:
            break
        try:
            numero1 = float(input('Informe o primeiro numero: '))
            numero2 = float(input('Informe o Segundo numero: '))
            print('')

            if menu == 1:
                print(adicao())
            elif menu == 2:
                print(subtracao())
            elif menu == 3:
                print(multiplicacao())
            elif menu == 4:
                print(divisao())
            else:
                print('Opção incorreta! ')
        except ValueError:
            print('Somente Numeros!! ')
    except ValueError:
        print('Operação informada incorreta, por favor informe o numero que representa a operação')