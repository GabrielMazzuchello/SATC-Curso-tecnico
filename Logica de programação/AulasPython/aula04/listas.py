task = ['estudar', 'fazer comida', 'caminhar', 'jogar', 'ler']
""" tesks = [1,2,5, 'estudar', True]

#acessando os itens da lista pelo o index
print(task[0])
print(task[1])
print(task[2])

#acessando os itens da lista invero pelo o index
print(task[-1])
print(task[-2])
print(task[-3])

print(task[0:5])
task.append('estudar fizica')
task.insert(0, 'dormir')
task.insert(5, 'jogar bola')

# remove usando o nome exato da lista
task.remove('jogar')
print(task)
# removee da lista usando o index
del task[0]
print(task)

# o pop sem parametro remove o ultimo item da lista
task.pop()

# o pop  remove o item da lista com o index e consegue armazenar em outra variavel
tarefas = task.pop(1)
print(task)
print(tarefas)
"""
# sort() ordena a lista de forma crecente ou ordem alfabética
"""values = [1,2,3,4,60,5,1,1]
values.sort()
print(values)
#reverte a lista
values.reverse()
print(values)

#tamanho da lista
print(len(values))

#maior e menor valor da lista
valor_max = max(values)
valor_min = min(values)
print(valor_max, valor_min)

# copia uma lista em uma nova lista
new_task = task.copy()

#limpa a lista
new_task.clear()

#conta quantos numeros iguais tem
print(values.count(1))

#inderx() retorna a posição do item
print(values.index(5))
new_list = []
new_list = values + task
print(new_list)"""

"""shopping = []
for c in range(5):
    produto = str(input('Digite o nome do produto: '))
    shopping.append(produto)
print(shopping)"""

lista_mercado = ['feijão', 'arroz', 'chocolate', 'leite', 'maça', 'café']
contador = 0
for c in lista_mercado:
    contador += 1
    print('{}: {}'.format((contador), c))