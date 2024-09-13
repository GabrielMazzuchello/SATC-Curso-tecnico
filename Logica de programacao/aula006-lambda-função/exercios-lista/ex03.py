
nameList = []

for c in range(5):
    name = input('Informe um nome: ')
    nameList.append(name)

print(list(filter(lambda x : 'a' in x, nameList)))