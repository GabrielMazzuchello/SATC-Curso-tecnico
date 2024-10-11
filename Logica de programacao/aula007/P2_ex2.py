funcionario = {}
salarioSoma = 0

def addFuncionario():
    global salarioSoma 
    nome = input('Informe o nome do funcionario: ')
    salario = float(input('Informe o salario do funcionario: '))
    salarioSoma += salario
    funcionario.update({nome: salario})

quant_funcionario = int(input('Quantos funcionarios a empresa possui: '))

for c in range(quant_funcionario):
    addFuncionario()

salarioFiltro = float(input('Informe o valor para filtrar os funcionarios: '))

funcionario_Filtrado = dict(filter(lambda x: x[1] > salarioFiltro, funcionario.items()))

funcionario_SalarioNovo = {nome: salario * 1.20 for nome, salario in funcionario_Filtrado.items()}

media_salarial = salarioSoma / quant_funcionario

print(f'A média salarial é {media_salarial}')

count = 0 
for nome, valor in funcionario.items():  
    if count == 0:
        maior = valor
        menor = valor
    elif valor < menor:
        menor = valor
    elif valor > maior:
        maior = valor
    count += 1

print(f'O funcionário com o maior salário ganha {maior} e o menor ganha {menor}')

print('Funcionários com salário acima do filtro e com 20% de aumento:')
for nome, salario in funcionario_SalarioNovo.items():
    print(f'{nome}: {salario:.2f}')
