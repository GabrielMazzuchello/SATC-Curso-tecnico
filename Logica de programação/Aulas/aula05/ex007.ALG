Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 14/03/2024
Var
// Seção de Declarações das variáveis 
nome, classificacao : caractere
idade : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Informe seu nome: ")
leia(nome)
escreval("Informe sua idade: ")
leia(idade)

escolha(idade)

caso 0 ate 3
     classificacao <- "Bebê"
   
caso 4 ate 11
     classificacao <- "Criança"

caso 12 ate 17
     classificacao <- "Adolescente"

caso 18 ate 60
     classificacao <- "Adulto"

caso 61 ate 99
     classificacao <- "3° Idade"

outrocaso
     escreval("Idade incorreta, tente novamente")
     
fimescolha

limpatela
escreval("",nome, "A classificação da sua idade é: ",classificacao)

Fimalgoritmo