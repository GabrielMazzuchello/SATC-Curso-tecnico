Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 14/03/2024
Var
// Se��o de Declara��es das vari�veis 
nome, classificacao : caractere
idade : inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Informe seu nome: ")
leia(nome)
escreval("Informe sua idade: ")
leia(idade)

escolha(idade)

caso 0 ate 3
     classificacao <- "Beb�"
   
caso 4 ate 11
     classificacao <- "Crian�a"

caso 12 ate 17
     classificacao <- "Adolescente"

caso 18 ate 60
     classificacao <- "Adulto"

caso 61 ate 99
     classificacao <- "3� Idade"

outrocaso
     escreval("Idade incorreta, tente novamente")
     
fimescolha

limpatela
escreval("",nome, "A classifica��o da sua idade �: ",classificacao)

Fimalgoritmo