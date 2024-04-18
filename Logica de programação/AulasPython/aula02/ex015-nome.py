nome = str(input('Informe seu nome: '))
escolha = str(input('Você gosta do seu nome (Sim) ou (Nao): ')).upper()

if escolha == "SIM":
    print('Que bom que você gosta do seu nome!')
elif escolha == "NAO" or "NÃO":
    print('Que pena que você não gosta do seu nome! :(')
else:
    print('Opção invalida')