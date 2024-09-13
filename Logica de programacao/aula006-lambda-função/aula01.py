"""print((lambda x :x ** 2) (9))
print((lambda x :x ** 3) (9))
print((lambda x,y :x ** y) (9, 9))

squared = lambda x, y: x ** y
print(squared(9, 2))"""

# mesma coisa do que antes só que com função def

"""def quadrado(x):
    return(x ** 2)

def cubo(x):
    return(x ** 3)
    
def potencia(x, y):
    return(x ** y)
    
print(quadrado(5))
print(cubo(5))
print(potencia(5,3))"""


"""name_age = lambda name, age: print(f'{name}, tem {age} anos')
names = input('Digite seu nome: ')
ages = int(input('Digite sua idade: '))

name_age(names, ages)"""

# lista de função lambda a qual é passada os valores para cada uma pelo for

"""equations = [
    lambda x, y : x / y,
    lambda x, y : x * y,
    lambda x, y : x ** y
]

valueX = int(input("Informe um numero inteiro: "))
valueY = int(input('informe outro valor: '))

for i in equations:
    print(i(valueX, valueY))"""

# =========================================================================
#  função filter (filtro)
# =========================================================================

"""numbers = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
]

for i in numbers:
    if i % 2 == 0:
        print(i)

print(list(filter(lambda x : x % 2 == 0, numbers)))"""


"""names = [
    'gabriel',
    'joao',
    'felipe',
    'lucas'
]

print(list(filter(lambda x : 'a' in x, names)))"""

# =========================================================================
# cusando o MAP

"""numbers = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
]

print(list(map(lambda x: x ** 2, numbers)))

names = [
    'gabriel',
    'joao',
    'felipe',
    'lucas'
]

print(list(map(lambda x : x.capitalize(), names)))
print(list(map(lambda x : len(x), (names))))

ordered = sorted(names, key=lambda x : len(x)) # muda o filtro para o tamanho de cada palavra
ordered = sorted(names, key=len) # mesma coisa que a linha anterior
ordered = sorted(names, reverse=True, key=len) # tudo igual só que reverso 
print(ordered)"""

# =========================================================================
            # função reduce() importar ela de functools

import functools

numbers = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10
]

print(functools.reduce(lambda x,y: x+y, numbers))
print(functools.reduce(lambda x,y: x if x < y else y, numbers))