# criando tuplas
minha_tupla = (1,2,3, 'Programação', True)
minha_tupla2 = (5,6,7,8, 'hello')
print(type(minha_tupla))

# assesando as tuplas
print(minha_tupla[1])

#fatiamento de tuplas
print(minha_tupla[:2]) # 1 e 2

# tamanho da tupla
print(len(minha_tupla))

# concatenando a tupla
print(minha_tupla+minha_tupla2)

# min e max
tupla_valor = (1,2,3,4,5,6,7,8,9)
print(min(tupla_valor))
print(max(tupla_valor))

print('')
# desenpacotamento de tripla
thirdTuple = (1, 2, 3)
x, y, z = thirdTuple
print(x)
print(y)
print(z)

# função enumerate

frutas = ('maça', 'banana', 'abacaxi', 'melancia')

print('')
for indice, i in enumerate(frutas, 1):
    print(f'{indice}: {i}')

print('')
#==============================DICIONARIO======================================

carros = {
    'Marca': 'Chevrolet',
    'modelo': 'onix',
    'ano': 2021,
    'placa': 'AB101',
    }

print(carros['Marca'])
print(carros['modelo'])

print(carros.get('ano'))
print(carros.get('placaq', 'Chave não encontrada'))
# acessando dados de um dicionario

# acessando as chaves
print(carros.keys())

# acessando as chaves e valores 
print(carros.items())

#atribuindo e alterando valores do dicionario
print('')
carros['placa2'] = 'AQM1010'
print(carros.items())
print('')
carros['placa2'] = 'AQM1010'
print(carros.items())

print('')
print('')
print('')

carros.update({'cor':'preto'})
print(carros.items())

a = carros.pop('cor')
print(a)

del carros['placa2']
print(carros.items())

# verificando se o item 
print('marca' in carros)
print('placa' in carros)

#iterando sobre os valores

for i in carros:
    print(i) # somente chaves

for i in carros.values():
    print() # somente valores

for i in carros.items():
    print(i) # chaves e valores

for chave, valor in carros.items():
    print(f'{chave}: {valor}')

escola ={
    'maria': 7.5,
    'joãzinho': 10,
    'jessica': 8.4
}

"""for aluno, nota in escola.items():
    print(f'{aluno}: {nota}')


filmes = {}
for c in range(3):
    # dicionario com imput
    

    name = input('Nome do filme: ')
    genre = input('digite o gênero: ')

    #filmes['nome'] = name
    #filmes['genero'] = genre

    filmes.update({'nome': name})
    filmes.update({'genero': genre})
print(filmes.items())
"""

"""locadora = [
    {'nome': 'up', 'genero': 'aventura'},
    {'nome': 'a freira', 'genero': 'horror'},
    {'nome': 'simp', 'genero': 'comedia'}
]
print(locadora[1]['nome'])
print(locadora[0].values())
print(locadora[0].keys())

"""


print('')
locadora = []
for c in range(3):
    filmes = {}

    name = input('Nome do filme: ')
    genre = input('digite o gênero: ')

    filmes.update({'nome': name})
    filmes.update({'genero': genre})
    locadora.append(filmes)

print(locadora)

for i in locadora:
    for chave, valor in i:
        print(f'{chave}: {valor}')