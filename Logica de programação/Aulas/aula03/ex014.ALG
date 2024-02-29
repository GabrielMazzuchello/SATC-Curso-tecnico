Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 29/02/2024
Var
// Seção de Declarações das variáveis 
precoproduto, acresimo, totalproduto : real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Informe o valor do produto: ")
leia(precoproduto)
limpatela
escreval("Informe o percentual(%) de acrecimo ao valor do produto: ")
leia(acresimo)
limpatela

totalproduto <- (precoproduto / 100 * acresimo) + precoproduto

escreval("O valor da venda do produto será de: ",totalproduto)



Fimalgoritmo