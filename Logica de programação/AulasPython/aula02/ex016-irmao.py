irmao = str(input('Você tem irmão? (sim) ou (Não): ')).upper()

if irmao == "SIM":
    quantidade = int(input('Quantos irmãos você tem?'))
    print('que legal você tem {} irmão(s), eu tenho um!'.format(quantidade))
elif irmao == "NAO" or "NÃO":
    print('Você gostaria de ter um irmão?')
else:
    print('Opção invalida')