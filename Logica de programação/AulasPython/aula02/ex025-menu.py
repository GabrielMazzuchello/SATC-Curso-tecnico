print(' escolha uma opção:')
print('1 - Soma \n 2 - Diferença entra dois numeros \n 3 - multiplicação \n 4 - Divisão')
escolha = int(input())

n1 = float(input('Informe um numero; '))
n2 = float(input('informe o segundo numero: '))


if escolha == 1:
    print('A soma dos numeros é {}'.format(n1+n2))
elif escolha == 2:
    print('A diferença entre o numero {} e o numero {} é {}'.format(n1))