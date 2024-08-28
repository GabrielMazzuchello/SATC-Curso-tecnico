""" def primeira_funcao():
    print('Primeira função')

primeira_funcao() """

""" def cores():
    cor1 = input('Digite uma cor: ')
    cor2 = input('Digite uma cor: ')
    print(f'as cores escolhidas {cor1} e {cor2}') """

""" def soma(a=0,b=0):
    s = a + b
    print(f'a soma dos valores {a} e {b} é {s}')

valor1 = float(input('Informe um valor: '))
valor2 = float(input('Informe um valor: '))
soma(valor1, valor2) """

""" def soma(*args):
    s = 0
    for i in args:
        s += i
        print(s)
soma(10,20,5,7,9) """

"""def pessoas(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')
    
nome = input('Informe seu nome: ')
idade = int(input('informe sua idade: '))
endereco = input('informe seu endereço: ')

pessoas(nome=nome, idade=idade, endereco=endereco) """

""" def somar(a, b):
    s = a + b
    m = a * b
    return s, m

soma, multiplicacao = somar(10, 20)

print(f'o resultado da soma é {soma} e da multiplicação {multiplicacao}') """


""" def par(n):
    if n % 2 == 0:
        return 'Esse valor é par' 
    else:
        return 'Esse valor é ímpar'

n = int(input('informe um numero: ')) 
print(par(n)) """

def soma(a=0,b=0):
    global s
    s = a + b
    return s

valor1 = float(input('Informe um valor: '))
valor2 = float(input('Informe um valor: '))

print(soma(valor1, valor2))
print(s) 


