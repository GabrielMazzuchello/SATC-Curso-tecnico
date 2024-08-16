"""Crie um programa PYTHON para um dicionário, contendo uma lista de informações, para cadastrar os Carros de uma revenda, seguindo a ordem:  
               Carros = { 1 : [ “fiat”, “palio”, “ano 2022”, “prata”], 
                          2 : [ “ford”, “fiesta”, “ano 2023”, “branca”],
                          3 : [ “honda”, “fit”, “ano 2024”, “preta”], etc }
Deve conter um MENU de opções para: 
1 – Cadastrar
2 – Excluir
3 – Pesquisar
4 - Sair
Para as opções de Cadastrar, Excluir e Pesquisar, perguntar antes qual codigo do carro deseja e verificar se já foi cadastrada
antes de realizar a operação. Mostrar depois o dicionario atualizado.
"""
Carros = {}
Count = 0


while True:
    print("""
    1 – Cadastrar
    2 – Excluir
    3 – Pesquisar
    4 - Sair """)
    menu = int(input('-> '))

    match menu:
        case 1:
            Marca = input('informe a marca do carro: ')
            Modelo = input('informe o modelo do carro: ')
            Ano = input('informe o ano do carro: ')
            Cor = input('informe a cor do carro: ')
            cadastro = [Marca, Modelo, Ano, Cor]
            Count += 1

            if len(Carros) <= 0:
                Carros.update({Count: cadastro})

            else:
                for i in len(Carros):
                    Carros.update({Count: cadastro})
        
        case 4:
            break


