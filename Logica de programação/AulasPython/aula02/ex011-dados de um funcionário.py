nome = str(input('Informe seu nome: '))
horastrabalhada = int(input('informe a quantidade de horas trabalhadas: '))
valorhora = float(input('Informe o valor por hora trabalhada: '))

salariofinal = (valorhora * horastrabalhada) * 0.98

print('{} seu salário final é de {}'.format(nome, salariofinal))