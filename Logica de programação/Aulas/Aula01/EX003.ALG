Algoritmo "ex003"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 15/02/2024
Var
// Seção de Declarações das variáveis 
nota1, nota2, media : real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Informe a primeira nota: ")
leia(nota1)
escreval("Informe a segunda nota: ")
leia(nota2)
limpatela

media <- (nota1 + nota2) / 2

se media < 7 entao
   escreval("Reprovado a media do aluno foi ",media)

senao
     escreval("Aprovado!!! a media do aluno foi ",media)
fimse

Fimalgoritmo