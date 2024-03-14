Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 14/03/2024
Var
// Seção de Declarações das variáveis
nome, situacao : caractere
peso, altura, imc : real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
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
escreval(nome, " Sua situação é: ",situacao)



Fimalgoritmo