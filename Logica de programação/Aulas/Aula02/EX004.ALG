Algoritmo "ex004"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/02/2024
Var
// Se��o de Declara��es das vari�veis
nome, produto : caractere
preco, quantidade, total : real


Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
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