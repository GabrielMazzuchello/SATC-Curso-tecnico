Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 29/02/2024
Var
// Se��o de Declara��es das vari�veis 
totalcompra, valorparcela : real
parcelas : inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc..
// Uma loja est� vendendo seus produtos em presta��es sem juros. Fa�a um programa que receba o valor de uma compra e o numero de parcelas e ap�s calcule e mostre o valor das presta��es.

escreval("Informe o valor total da sua compra: ")
leia(totalcompra)
limpatela
escreval("Informe em quantas vezes deseja parcelar: ")
leia(parcelas)
limpatela

valorparcela <- totalcompra / parcelas

escreval("O valor de cada parcela ficou de: ",valorparcela)

Fimalgoritmo