
produtos = {}

def adicionarProduto():
    nome = input('Informe o nome do produto: ')
    estoque = int(input('Informe a quantidade em estoque: '))
    produtos[nome] = estoque

def attEstoque():
    nome = input('Informe o nome do produto: ')
    estoque = int(input('Informe a quantidade em estoque: '))
    produtos[nome] = estoque

def visualizar():
    print(produtos)

def excluirProduto():
    i = input('Informe o produto que queira excluir: ')
    del produtos[i]

def consultarProduto():
    nome = input('Informe o nome do produto: ')
    print(produtos[nome])



while True:
    op = int(input("""-=-=-Menu-=-=-
1 - Cadastrar produto
2 - Atualizar estoque
3 - Remover produto
4 - Visualizar estoque
5 - Consultar produto   
6 - Sair \n"""))
    
    if op == 1:
        adicionarProduto()

    elif op == 2:
        attEstoque()
    
    elif op == 3:
        excluirProduto()
    
    elif op == 4:
        visualizar()
    
    elif op == 5:
        consultarProduto()

    elif op == 6:
        break

    else:
        print('Opcão errada')

        
