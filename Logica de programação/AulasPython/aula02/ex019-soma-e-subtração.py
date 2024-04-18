n1 = float(input('infome um numero: '))
n2 = float(input('informe outro numero: '))
opcao = input('quer reaalizar a operação de (-) subtração ou de (+) adição: ')

if opcao == '-':
    print('O resultado da subtração do numero {} e do numero {} é {}'.format(n1, n2, (n1-n2)))
elif opcao == '+':
    print('O resultado da adição do numero {} e do numero {} é {}'.format(n1, n2, (n1+n2)))
else:
    print('opção invalida')