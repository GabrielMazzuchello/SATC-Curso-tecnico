Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 29/02/2024
Var
// Se��o de Declara��es das vari�veis
nome : caractere
salariofixo, totalvendas, salariototal : real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc...
escreval("Informe o nome do funcionario: ")
leia(nome)
limpatela
escreval("Informe o salario fixo do funcionario: ")
leia(salariofixo)
limpatela
escreval("Informe o total de vendas(R$) do funcionario: ")
leia(totalvendas)
limpatela

salariototal <- totalvendas * 0.15 + salariofixo

escreval("O salario fixo do funcionario �: ",salariofixo, " e o salario total desse mes � de:",salariototal)


Fimalgoritmo