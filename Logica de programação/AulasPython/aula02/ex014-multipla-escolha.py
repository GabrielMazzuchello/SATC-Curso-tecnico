print('Qual é o resultado da multiplicação 9 * 5 = ?')
print(' 1- 45 \n 2- 38 \n 3- 30 \n 4- 50 ')
escolha = int(input('Digite sua escolha (1,2,3 ou 4): '))

if escolha == 1:
    print('Parabens!!! Você acertou')
elif (escolha == 2) or (escolha == 3) or (escolha == 4):
    print('Você errou tente novamente!')
else:
    print('Opção invalida')