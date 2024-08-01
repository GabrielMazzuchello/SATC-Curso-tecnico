""" Desenvolva um programa em Python que apresente um menu interativo com as
seguintes opções:
a. Adicionar um número: Permita ao usuário adicionar um número à lista.
b. Remover um número: Permita ao usuário remover um número específico da
lista.
c. Exibir todos os números: Liste todos os números atualmente na lista.
d. Exibir somente números pares: Liste apenas os números pares presentes na
lista, um embaixo do outro.
e. Exibir somente números ímpares: Liste apenas os números ímpares
presentes na lista, um embaixo do outro.
f. Exibir somente números primos: Liste apenas os números primos presentes
na lista, um embaixo do outro."""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

nunbers = []

while True:
    print("""Menu:
    1- Adicionar um número
    2- Remover um número
    3- Exibir todos os números
    4- Exibir somente números pares
    5- Exibir somente números ímpares
    6- Exibir somente números primos
""")
    menu = int(input('->')).strip()

    match menu:
        case 1:
            nunber = int(input('Informe o valor INTEIRO que desejá adicionar: '))
            nunbers.append(nunber)
        
        case 2:
            try:
                nunber = int(input('Informe o número para remover: '))
                if nunber in nunbers:
                    nunbers.remove(nunber)
                else:
                    print('Número não encontrado na lista.')
            except ValueError:
                print('Informe um número válido.')
        case 3:
            if nunbers:
                print("\nTodos os números:")
                for num in nunbers:
                    print(num)
            else:
                print("Nenhum número na lista.")
        case 4:
            pares = [num for num in nunbers if num % 2 == 0]
            if pares:
                print("Números pares:")
                for num in pares:
                    print(num)
            else:
                print("Nenhum número par na lista.")
        case 5:
            impares = [num for num in nunbers if num % 2 != 0]
            if impares:
                print("Números ímpares:")
                for num in impares:
                    print(num)
            else:
                print("Nenhum número ímpar na lista.")
        case 6:
            primos = [num for num in nunbers if is_prime(num)]
            if primos:
                print("\nNúmeros primos:")
                for num in primos:
                    print(num)
            else:
                print("Nenhum número primo na lista.")
        case 7:
            break
        