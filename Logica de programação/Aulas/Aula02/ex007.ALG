Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/02/2024
Var
// Se��o de Declara��es das vari�veis 
nome : caractere
idade, peso, altura, massa : real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Informe seu nome: ")
leia(nome)
escreval("Informe sua idade: ")
leia(idade)
escreva("Informe sua peso: ")
leia(peso)
escreval("Informe sua altura para ser feito o cauculo do seu indice de massa corporal")
leia(altura)

massa <- peso / (altura * altura)

escreval("Seu IMC (Indice de massa corporal) �: ",massa:5:2)
Fimalgoritmo