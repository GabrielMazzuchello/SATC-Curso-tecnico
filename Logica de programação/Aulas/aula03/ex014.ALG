Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 29/02/2024
Var
// Se��o de Declara��es das vari�veis 
precoproduto, acresimo, totalproduto : real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Informe o valor do produto: ")
leia(precoproduto)
limpatela
escreval("Informe o percentual(%) de acrecimo ao valor do produto: ")
leia(acresimo)
limpatela

totalproduto <- (precoproduto / 100 * acresimo) + precoproduto

escreval("O valor da venda do produto ser� de: ",totalproduto)



Fimalgoritmo