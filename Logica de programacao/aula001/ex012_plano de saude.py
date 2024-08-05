"""Uma empresa deseja conceder aos seus funcionários direito ao plano de saúde.
Faça um algoritmo que receba como entrada os dados dos funcionários: nome do
cliente, idade, valor do plano. Calcule e mostre o novo valor a ser pago, de acordo
com a tabela abaixo:
Faixa Etária Aumento
De 0 a 18 anos 5%
De 19 a 35 anos 10%
De 36 a 60 anos 15%
Acima de 60 anos 20%
"""
name = input('Informe o nome: ')
age = int(input('Informe sua idade: '))
value = float(input('Informe o valor do plano: '))

if 0 <= age <= 18:
    amount = value * 1.05

elif 19 <= age <= 35:
    amount = value * 1.10

elif 36 <= age <= 60:
    amount = value * 1.15

elif age > 60:
    amount = value * 1.20

else:
    print('Idade invalida!')

print(f'O novo valor do plano é de {amount}')