Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 21/03/2024
Var
// Se��o de Declara��es das vari�veis
menu : inteiro
celcios, convercao : real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc...
escreval("============================")
escreval(" 1- Celsius para Kelvin")
escreval(" 2- Celsius para Fahrenheit ")
escreval(" 3- Celsius para R�aumur")
escreval("============================")
leia(menu)

escreval("informe a temperatura �C: ")
leia(celcios)

escolha(menu)
caso 1
     convercao <- (celcios + 273.15)
caso 2
     convercao <- (celcios * 1.8 + 32)
caso 3
     convercao <-  (celcios * 0.8)
fimescolha

escreval("A temperatura comvertida � de: ",convercao)


Fimalgoritmo