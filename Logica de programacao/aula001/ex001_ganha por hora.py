ValorHora = int(input('Informe o valor que você recebe por hora: '))
HorasMes = int(input('Informe a quantidade de horas que você trabalha por mes: '))

SalarioBruto = ValorHora * HorasMes

Inss = SalarioBruto * 0.08
Ir = SalarioBruto * 0.11
Sindicato = SalarioBruto * 0.05

SalarioLiquido = SalarioBruto - (Inss + Ir + Sindicato)

print(f'O salario bruto é {SalarioBruto:.2f}')
print(f'O valor do INSS é {Inss:.2f}')
print(f'O valor do Sindicado é {Sindicato:.2f}')
print(f'O valor do IR é de {Ir:.2f}')
print(f'O valor do salario liquido é {SalarioLiquido:.2f}')
