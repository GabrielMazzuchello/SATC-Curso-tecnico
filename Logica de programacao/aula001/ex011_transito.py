"""11) Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre
acidentes de trânsito. Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999).
Deseja-se saber:
a. Qual o maior e menor índice de acidentes de trânsito e a que cidade
pertence;
b. Qual a média de veículos nas cinco cidades juntas;
c. Qual a média de acidentes de trânsito nas cidades com menos de 2.000
veículos de passeio.
"""

# exercicio comfuzo pois diz que foi obtido dados mas não diz o que e não é mencionado se o usuario do programa é quem digitaria os valores
# então fiz com dados ipotéticos e com cidades ipotéticas e pesquisei para fazer inclusive no chat gpt e o pedi para explicar o codigo já que não entendo o que estava sendo pedido


cidades = [
    {"nome": "Goiânia", "veiculos": 1500, "acidentes": 10},
    {"nome": "Vitória", "veiculos": 2500, "acidentes": 15},
    {"nome": "Manaus", "veiculos": 3000, "acidentes": 8},
    {"nome": "Florianópolis", "veiculos": 1800, "acidentes": 12},
    {"nome": "Belém", "veiculos": 2200, "acidentes": 20}
]

menor_acidente = float('inf')
maior_acidente = float('-inf')
cidade_menor_acidente = ""
cidade_maior_acidente = ""
total_veiculos = 0
total_acidentes_menos_2000 = 0
cidades_menos_2000 = 0

for cidade in cidades:
    veiculos = cidade["veiculos"]
    acidentes = cidade["acidentes"]
    
    if acidentes < menor_acidente:
        menor_acidente = acidentes
        cidade_menor_acidente = cidade["nome"]
    if acidentes > maior_acidente:
        maior_acidente = acidentes
        cidade_maior_acidente = cidade["nome"]
    
    total_veiculos += veiculos
    if veiculos < 2000:
        total_acidentes_menos_2000 += acidentes
        cidades_menos_2000 += 1

media_veiculos = total_veiculos / len(cidades)
if cidades_menos_2000 > 0:
    media_acidentes_menos_2000 = total_acidentes_menos_2000 / cidades_menos_2000
else:
    media_acidentes_menos_2000 = 0

# Exibição dos resultados
print(f"Maior índice de acidentes: {maior_acidente} na cidade de {cidade_maior_acidente}")
print(f"Menor índice de acidentes: {menor_acidente} na cidade de {cidade_menor_acidente}")
print(f"Média de veículos nas cinco cidades: {media_veiculos:.2f}")
print(f"Média de acidentes nas cidades com menos de 2.000 veículos: {media_acidentes_menos_2000:.2f}")
