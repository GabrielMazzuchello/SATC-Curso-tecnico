Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 07/03/2024
Var
// Se��o de Declara��es das vari�veis 
nome : caractere
idade : inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Informe seu nome: ")
leia(nome)

escreval("Informe sua idade: ")
leia(idade)

se idade < 18 entao
   escreval("Voce ",nome, " � de menor de idade")
senao
   escreval("Voce ",nome, " � de maior de idade")
fimse
   
Fimalgoritmo