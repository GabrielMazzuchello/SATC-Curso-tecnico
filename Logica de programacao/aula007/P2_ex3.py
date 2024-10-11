
pedidos = {}


def addpedidos(): 
    listaPedidos = []
    nome = input('Infprme o nome do cliente: ') 
    pedido = input('Informe o nome do prato: ')
    listaPedidos.append(pedido) 
    pedidos.update({nome: listaPedidos})

def attpedido():
    nome = input('Qual cliente deseja modificar o pedido: ') 
    pedido = input('Informe o nome do prato: ')
    
    for chave, valor in pedidos.items():
        if chave == nome:
            listaPedidos = valor
            
    if pedido in listaPedidos:
        print('ERRO: o pedido já esta na lista!') 
    else:
        listaPedidos.append(pedido)
        pedidos.update({nome: listaPedidos})

def excluirpedidos(): 
    nome = input('Digite o nome do cliente que deseja excluir o pedido: ')
    pedido = input('Qual o nome do pedido que você quer excluir? ')

    for chave, valor in pedidos.items():
        if chave == nome: 
            listaPedidos = valor

    if pedido in listaPedidos:
        listaPedidos.remove(pedido) 
        pedidos.update({nome: listaPedidos})
        
    else:
        print('ERRO: o pedido não esta na lista!')

def filtrarpedidos():
    nome = input('Digite o nome do cliente que deseja mostrar os pedidos: ')

    for chave, valor in pedidos.items():
        if chave == nome:
            listaPedidos = valor
    print('Os pedidos são: ') 
    for c in listaPedidos:
        print(c)

def visualizar(): 
    for chave, valor in pedidos.items():
        print(f'O cliente {chave}:')
        print('Os pedidos são: ')
        for c in valor:
            print(c)
    
        
    
while True:  
    print("""1- Adicionar pedido
2- Atualizar pedido
3- Remover pedido 
4- Filtrar pedido
5- Visualizar todos os pedidos
6- Sair""")
    opcao = int(input()) 
    
    if opcao == 1: 
        addpedidos()

    elif opcao == 2:
        attpedido()

    elif opcao == 3:
        excluirpedidos()

    elif opcao == 4:
        filtrarpedidos()
        
    elif opcao == 5:
        visualizar()
    
    elif opcao == 6:
        print("Volte sempre!!")
        break




