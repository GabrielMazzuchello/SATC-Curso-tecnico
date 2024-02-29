Algoritmo "ex01"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 29/02/2024
Var
// Seção de Declarações das variáveis 
nome : caractere
horastrabalhada, valorhora, salariosujo, salariototal : real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Informe o nome do funcionario: ")
leia(nome)
escreval("Informe o total de horas trabalhadas: ")
leia(horastrabalhada)
escreval("Informe o valor por hora a ser pago ao funcionario: ")
leia(valorhora)
limpatela

salariosujo <- horastrabalhada * valorhora
salariototal <- salariosujo * 0.98

escreval("O salario do funcionario: ",nome, " nesse mez é de R$ ",salariototal,)


Fimalgoritmo