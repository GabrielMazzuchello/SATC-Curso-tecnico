"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol. Depois mostre:
    Apenas os 5 primeiro colocados;
    Os últimos 4 colocados da tabela;
    Uma lista com os times em ordem alfabética;
    Em que posição na tabela está o time da Criciuma.
"""
teams = ("Botafogo", "Fortaleza", "Flamengo", "Palmeiras", "São Paulo", "Cruzeiro", "Bahia", "Athletico-PR", "Atlético-MG", "Vasco", 
         "Bragantino", "Juventude", "Grêmio", "Criciúma", "Internacional", "Vitória", "Corinthians", "Fluminense", "Cuiabá", "Atlético-GO")

time = []

for c in range(5):
    print(f"Os cinco primeiros times são: {teams[c]}")
    
print(f'os ultimos quatro colocados são: {teams[16]} {teams[17]} {teams[18]} {teams[19]}')

for i in teams:
    time.append(i)

time.sort()
print(time)

for i, c in enumerate (teams):
    if c == "Criciúma":
        print(i+1)
        