lista = []
repetidos = []

for i in range(5):
    item = input('Digite o item a ser inserido na lista: ')
    lista.append(item)
for i in lista:
    if lista.count(i) > 1:
        if i not in repetidos:
            repetidos.append(i)

for i in repetidos:
    print(f'{i}: {lista.count(i)}')


