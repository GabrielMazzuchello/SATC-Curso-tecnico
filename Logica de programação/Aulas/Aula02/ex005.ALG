Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/02/2024
Var
// Se��o de Declara��es das vari�veis 
nome, cargo : caractere
salario, salariototal, percentual : real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Informe o nome do funcionario: ")
leia(nome)
escreval("Informe o cargo do funcionario: ")
leia(cargo)
escreval("Informe o sal�rio do funcionario: ")
leia(salario)
escreval("Informe o percentual que desej� dar de almento: ")
leia(percentual)
limpatela

salariototal <- (salario / 100 * percentual) + salario

escreval("O salario do funcionario ",nome," do cargo ",cargo," agora � de: ",salariototal)


Fimalgoritmo