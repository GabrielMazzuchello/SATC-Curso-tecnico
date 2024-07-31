"""Elabore um algoritmo que leia nome do produto, quantidade, preço e o Tipo de
pagamento. Após calcule e mostre o valor final a ser pago considerando a escolha
da condição de pagamento. Utilize as condições de pagamento da tabela a seguir:
Tipo Pagamento Condição
1 À vista em dinheiro recebe 10% de desconto
2 À vista no cartão de crédito, recebe 5% de desconto
3 Em duas vezes, preço normal sem juros
4 Em três vezes, preço normal mais juros de 5% acréscimo"""

ProductName = input('Informe o nome do produto: ')
Amount = int(input('Informe a quantidade do produto: '))
Price = float(input('Informe o preço do produto: '))

PurchasePrice = Amount * Price

print('''Escolha o metodo de pagamente:
      1- À vista em dinheiro recebe 10% de desconto
      2- À vista no cartão de crédito, recebe 5% de desconto
      3- Em duas vezes, preço normal sem juros
      4- Em três vezes, preço normal mais juros de 5% acréscimo
''')
menu = int(input('-> '))

if menu == 1:
    TotalPrice = PurchasePrice - (PurchasePrice * 0.10)
    print(f'O valor total da sua compra é de {TotalPrice:.2f}')

elif menu == 2:
    TotalPrice = PurchasePrice - (PurchasePrice * 0.05)
    print(f'O valor total da sua compra é de {TotalPrice:.2f}')

elif menu == 3:
    TotalPrice = PurchasePrice / 2
    print(f'O valor de cada uma das suas parcelas é de {TotalPrice:.2f}')

elif menu == 4:
    Portion = PurchasePrice / 3
    TotalPrice = Portion + (Portion * 1.05) * 1.05
    print(f'O valor total da sua compra é de{TotalPrice:.2f}')

    
