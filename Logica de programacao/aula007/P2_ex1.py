listaMeses = ['janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
receitas = []
despesas = []
meses_prejuiso2 = {}

contador = 0 

for c in range(12):
    receita = float(input("Informe a receita do mes: "))
    despesa = float(input("Informe as despesas do mes: "))
    receitas.append(receita)
    despesas.append(despesa) 
    contador += 1

    lucroMes = list(map(lambda x,y : x - y, receitas, despesas)) 
    meses_prejuiso = list(filter(lambda x : x if x < 0 else False , lucroMes)) 
    


lucro_medio_anual = sum(lucroMes) / 12 



for c in lucroMes: 
    print(f'O lucro mensal foi de: {c}')

for i, c in enumerate(lucroMes): 
    if c < 0:
        print(f'O mes {listaMeses[i]} deu prejuiso de {c}')

print(f'O lucro medio anual foi de: {lucro_medio_anual}')


