kg = float(input('Informe seu peso (kg): '))
altura = float(input('Informe sua altura: '))
imc = kg / (altura ** 2)

print('')
print('O IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Está abaixo do peso!!')
elif 18.5 <= imc < 25:
    print('Peso ideal.')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')