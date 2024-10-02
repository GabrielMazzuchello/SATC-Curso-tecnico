# aluno: Gabriel Mazzuchello Dal Molin Turma: 2137  Data: 18/09/2024
# aluno: João Alejandro Brenis Borges

funcionario = {}        # Cria um dicionário
salarioSoma = 0

def addFuncionario():       #Função que adiciona funcionarios
    nome = input('Informe o nome do funcionario: ')     #Variável que recebe o nome do funcionario
    salario = float(input('Informe o salario do funcionario: ')) # recebe o salario do mesmo
    salarioSoma += salario # faz a soma do salario para descobrir a media
    funcionario.update({nome: salario}) # adiciona o funcionario com seu respectivo salario

quant_funcionario = int(input('Quantos funcionarios a empresa possui: ')) # pergunta quantos funcionarios a empresa tem

for c in range(quant_funcionario):         #Percorre a quantidade de funcionarios digitados
    addFuncionario() # chama a função addFuncionario

salarioFiltro = float(input('Informe o valor para filtrar os funcionarios: ')) # recebe o valor para filtrar os funcionarios

funcionario_Filtrado = dict(filter(lambda x: x if x[1] > salarioFiltro else False, funcionario.items())) # filtra os funcionarios de acordo com o valor digitado

# funcionario_SalarioNovo = dict(map(lambda x : x[0] (x[1] * 1.20), funcionario_Filtrado.items())) Não funciona deveria acrecentar 20% ao salario do funcionario

media_salarial = salarioSoma / quant_funcionario # caucula a media dos funcionarios

print(f'A media salarial é {media_salarial}')

count = 0 # contador para saber que essa é a primeira vez execultando o codigo para definir o maior e menor pela 1° vez
for nome, valor in funcionario.items(): # percorre o dicionario funcionario
    if count == 0:
        maior = valor  # todo o bloco até a linha 40 servem para verificar o maior e o menor valor
        menor = valor

    elif valor < menor:
        menor = valor

    elif valor > maior:
        maior = valor

    count += 1

print(f'O funcionario com o maior salario é {maior} e o menor é {menor}')

