TupValores = ()
VetPares = []
VezesNove = vezes = soma = maior = menor = contador = 0
mensagem = ''


for c in range(4):
    valor = int(input('Informe um valor: '))
    TupValores = TupValores + (valor,)

for index, valor in enumerate(TupValores):

    if valor == 9:
        VezesNove += 1
    
    if valor == 3 and vezes == 0:
        vezes += 1
        print(f'O numero 3 aparece primeiro na posição {index+1}')
    elif 3 not in TupValores:
        mensagem = 'O numero 3 não foi encontrado'
    
    if valor % 2 == 0:
        VetPares.append(valor)

    soma += valor
    media = soma / 4

    contador += 1
    if contador == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor

        if valor < menor:
            menor = valor   

print(f'O numero de vezes que aparece o numero 9 é {VezesNove}')
print(mensagem)
print(f'os numeros que são pares é {VetPares}')
print(f'A soma é {soma} e a média dos valores é {media}')
print(f'o maior valor é {maior}  e o menor valor é {menor}')
