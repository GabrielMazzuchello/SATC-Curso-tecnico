# aluno: Gabriel Mazzuchello Dal Molin Turma: 2137  Data: 18/09/2024
# aluno: João Alejandro Brenis Borges

# declaração das listas
listaMeses = ['janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
receitas = []
despesas = []
meses_prejuiso2 = {}

contador = 0 

for c in range(12): # percorre os 12 meses do ano perguntando o valor da despesa e da receita 
    receita = float(input("Informe a receita do mes: "))
    despesa = float(input("Informe as despesas do mes: "))
    receitas.append(receita) # adiciona o valor a lista receitas
    despesas.append(despesa) # adiciona o valor a lista despesas
    contador += 1

    lucroMes = list(map(lambda x,y : x - y, receitas, despesas)) # calcula o lucro do mês
    meses_prejuiso = list(filter(lambda x : x if x < 0 else False , lucroMes)) # calcula os meses que deram prejuiso
    


lucro_medio_anual = sum(lucroMes) / 12 # caucula o lucro medio anual



for c in lucroMes: # mostra o lucro dos meses 
    print(f'O lucro mensal foi de: {c}')

for i, c in enumerate(lucroMes): # mostra os meses em que ouve prejuiso
    if c < 0:
        print(f'O mes {listaMeses[i]} deu prejuiso de {c}')

print(f'O lucro medio anual foi de: {lucro_medio_anual}') # mostra para o usuario o lucro medio anual


