Algoritmo "ex01"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 29/02/2024
Var
// Se��o de Declara��es das vari�veis 
nome : caractere
horastrabalhada, valorhora, salariosujo, salariototal : real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Informe o nome do funcionario: ")
leia(nome)
escreval("Informe o total de horas trabalhadas: ")
leia(horastrabalhada)
escreval("Informe o valor por hora a ser pago ao funcionario: ")
leia(valorhora)
limpatela

salariosujo <- horastrabalhada * valorhora
salariototal <- salariosujo * 0.98

escreval("O salario do funcionario: ",nome, " nesse mez � de R$ ",salariototal,)


Fimalgoritmo