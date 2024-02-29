Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 29/02/2024
Var
// Seção de Declarações das variáveis 
deposito, juros, total : real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Informe o valor do seu deposito: ")
leia(deposito)
limpatela

juros <- 1.015
total <- deposito * juros

escreval("O total com o rendimento foi de R$: ",total, " e o juros foi de: 0,015%")

Fimalgoritmo