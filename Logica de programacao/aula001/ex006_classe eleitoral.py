"""Elabore um algoritmo que a partir do nome e da idade informada de uma pessoa,
verifique e mostre a sua classe eleitoral, sabendo que:
Menores de 16 não votam (não votantes)
Voto é obrigatório para adultos entre 18 e 65 anos (eleitor obrigatório)
Voto é opcional para eleitores com 16, 17 ou mais que 65 anos (eleitor
facultativo)."""

name = input('Informe seu nome: ')
age = int(input('Informe sua idade'))

if age < 16:
    print('Você não pode votar ainda não possui idade nescessaria')
elif 18 <= age <= 65:
    print('Você é obrigado a votar!')
elif age == 16 or age == 17 or age > 65:
    print('Seu voto é facultativo e não obrigatório')