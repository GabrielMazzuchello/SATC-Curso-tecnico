Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 14/03/2024
Var
// Se��o de Declara��es das vari�veis
nome, situacao : caractere
peso, altura, imc : real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc...
escreval("Informe seu nome: ")
leia(nome)
escreval("Informe sua altura: ")
leia(altura)
escreval("Informe seu peso: ")
leia(peso)

imc <- peso / (altura * altura)

escolha(imc)
caso 0 ate 18.4
     situacao <- "abaixo do peso"
caso 18.5 ate 25
     situacao <- "peso normal"
caso 25 ate 30
     situacao <- "acima do peso"
caso 30 ate 40
     situacao <- "obeso"
fimescolha

limpatela
escreval(nome, " Sua situa��o �: ",situacao)



Fimalgoritmo