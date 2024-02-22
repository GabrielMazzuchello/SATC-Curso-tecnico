Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/02/2024
Var
// Seção de Declarações das variáveis 
nome, cargo : caractere
salario, salariototal, percentual : real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Informe o nome do funcionario: ")
leia(nome)
escreval("Informe o cargo do funcionario: ")
leia(cargo)
escreval("Informe o salário do funcionario: ")
leia(salario)
escreval("Informe o percentual que desejá dar de almento: ")
leia(percentual)
limpatela

salariototal <- (salario / 100 * percentual) + salario

escreval("O salario do funcionario ",nome," do cargo ",cargo," agora é de: ",salariototal)


Fimalgoritmo