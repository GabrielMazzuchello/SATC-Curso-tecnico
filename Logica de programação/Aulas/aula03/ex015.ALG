Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 29/02/2024
Var
// Seção de Declarações das variáveis
nome : caractere
salariofixo, totalvendas, salariototal : real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
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

escreval("O salario fixo do funcionario é: ",salariofixo, " e o salario total desse mes é de:",salariototal)


Fimalgoritmo