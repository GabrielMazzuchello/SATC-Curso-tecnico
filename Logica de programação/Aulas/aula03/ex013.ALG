Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 29/02/2024
Var
// Seção de Declarações das variáveis 
totalcompra, valorparcela : real
parcelas : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc..
// Uma loja está vendendo seus produtos em prestações sem juros. Faça um programa que receba o valor de uma compra e o numero de parcelas e após calcule e mostre o valor das prestações.

escreval("Informe o valor total da sua compra: ")
leia(totalcompra)
limpatela
escreval("Informe em quantas vezes deseja parcelar: ")
leia(parcelas)
limpatela

valorparcela <- totalcompra / parcelas

escreval("O valor de cada parcela ficou de: ",valorparcela)

Fimalgoritmo