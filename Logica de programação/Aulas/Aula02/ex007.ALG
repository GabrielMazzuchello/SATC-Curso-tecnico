Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/02/2024
Var
// Seção de Declarações das variáveis 
nome : caractere
idade, peso, altura, massa : real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Informe seu nome: ")
leia(nome)
escreval("Informe sua idade: ")
leia(idade)
escreva("Informe sua peso: ")
leia(peso)
escreval("Informe sua altura para ser feito o cauculo do seu indice de massa corporal")
leia(altura)

massa <- peso / (altura * altura)

escreval("Seu IMC (Indice de massa corporal) é: ",massa:2)
Fimalgoritmo