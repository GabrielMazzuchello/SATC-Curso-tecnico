Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 07/03/2024
Var
// Seção de Declarações das variáveis 
nome : caractere
idade : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Informe seu nome: ")
leia(nome)

escreval("Informe sua idade: ")
leia(idade)

se idade < 18 entao
   escreval("Voce ",nome, " é de menor de idade")
senao
   escreval("Voce ",nome, " é de maior de idade")
fimse
   
Fimalgoritmo