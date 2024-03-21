Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 21/03/2024
Var
// Seção de Declarações das variáveis
menu : inteiro
celcios, convercao : real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
escreval("============================")
escreval(" 1- Celsius para Kelvin")
escreval(" 2- Celsius para Fahrenheit ")
escreval(" 3- Celsius para Réaumur")
escreval("============================")
leia(menu)

escreval("informe a temperatura °C: ")
leia(celcios)

escolha(menu)
caso 1
     convercao <- (celcios + 273.15)
caso 2
     convercao <- (celcios * 1.8 + 32)
caso 3
     convercao <-  (celcios * 0.8)
fimescolha

escreval("A temperatura comvertida é de: ",convercao)


Fimalgoritmo