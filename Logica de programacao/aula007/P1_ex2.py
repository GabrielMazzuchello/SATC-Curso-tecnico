MatCarros = {}
contador = 0

while True:
    print("""--------Menu--------
1- Cadastrar
2- Alterar
3- Excluir
4- Pesquisar
5- Sair
--------Menu--------""")
    opcao = int(input(''))

    if opcao == 1:
        contador += 1
        marca = input('informe a marca do carro: ')
        nomeCarro = input('informe o nome do carro: ') 
        ano = int(input('Informe o ano do carro: '))
        cor = input('informe a cor do carro: ')

        MatCarros.update({contador: [marca, nomeCarro, ano, cor]})

    elif opcao == 2:
        codigo = int(input('informe o codigo do carro: '))

        if codigo in MatCarros:
            alteracao = int(input('O que desejá alterar:\n1- Marca \n2- Nome \n3- Ano \n4- Cor\n'))

            if alteracao == 1:
                nova_marca = input('Digite a nova marca do carro: ')
                MatCarros[codigo][0] = nova_marca
            elif alteracao == 2:
                novo_nome = input('Digite o novo nome do carro: ')
                MatCarros[codigo][1] = novo_nome
            elif alteracao == 3:
                novo_ano = int(input('Digite o novo ano do carro: '))
                MatCarros[codigo][2] = novo_ano
            elif alteracao == 4:
                novo_cor = input('Digite a nova cor do carro: ')
                MatCarros[codigo][2] = novo_cor
            else:
                print('Opção invalida!! ')
        
        else:
            print('Carro não está cadastrado')
                

    elif opcao == 3:
        codigoExcluir = int(input('informe o codigo do carro que queira excluir: '))

        if codigoExcluir in MatCarros:
            del MatCarros[codigoExcluir]
        else:
            print('O codigo do carro não existe')
    
    elif opcao == 4:
        for i in sorted(MatCarros):
            print(f'Codigo: {i} Informação: {MatCarros[i]}')

    elif opcao == 5:
        break