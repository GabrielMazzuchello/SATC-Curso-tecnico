"""Numa eleição existem três candidatos identificados pelos números 1, 2 e 3. Faça
um algoritmo que compute o resultado de uma eleição.
a. Inicialmente o programa deve pedir o número total de votantes.
b. Em seguida, deve pedir para cada votante votar (informando o número do
candidato)
c. e ao final mostrar o número de votos de cada candidato"""
one = 0
two = 0
three = 0
voters = int(input('Informe o total de votantes: '))

for c in range(voters):
    vote = int(input('Informe o candidato que deseja votar (1, 2, 3)'))
    if vote == 1:
        one += 1
    elif vote == 2:
        two += 1
    elif vote == 3:
        three += 1
print(f'O candidato one teve {one} votos') 
print(f'O candidato two teve {two} votos') 
print(f'O candidato three teve {three} votos') 