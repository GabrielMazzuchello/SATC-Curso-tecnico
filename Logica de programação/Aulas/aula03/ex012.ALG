Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 29/02/2024
Var
// Se��o de Declara��es das vari�veis 
deposito, juros, total : real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Informe o valor do seu deposito: ")
leia(deposito)
limpatela

juros <- 1.015
total <- deposito * juros

escreval("O total com o rendimento foi de R$: ",total, " e o juros foi de: 0,015%")

Fimalgoritmo