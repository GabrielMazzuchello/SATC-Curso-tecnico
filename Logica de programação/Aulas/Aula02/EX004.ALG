Algoritmo "ex004"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/02/2024
Var
// Seção de Declarações das variáveis
nome, produto : caractere
preco, quantidade, total : real


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Informe o nome do cliente: ")
leia(nome)
escreval("Informe o nome do produto: ")
leia(produto)
escreval("Informe o valor do produto: ")
leia(preco)
escreval("Informe a quantidade: ")
leia(quantidade)

total <- quantidade * preco

escreval("O cliente ",nome," comprou ",quantidade," unidades de ",produto,"o valor total da compra foi de: ",total)

Fimalgoritmo