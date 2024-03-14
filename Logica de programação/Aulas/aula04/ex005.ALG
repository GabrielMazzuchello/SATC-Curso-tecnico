Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 07/03/2024
Var
// Seção de Declarações das variáveis
nota1, nota2, nota3, media : real
menu : inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
repita
escreval("")
escreval("=   1  Calculo da media     =")
escreval("=   2  sair do programa     =")
leia(menu)

escolha(menu)
caso 1
     limpatela
     escreval("Informe a primeira nota do aluno: ")
     leia(nota1)
     escreval("Informe a segunda nota do aluno: ")
     leia(nota2)
     escreval("Informe a terceira nota do aluno: ")
     leia(nota3)
     limpatela

     media <- (nota1 + nota2 + nota3) / 3

     se media >= 7 entao
        escreval("O aluno foi aprovado, com média de: ",media:2:2)
     senao
          se (5 < media) e (media < 7) entao
             escreval("O aluno esta em recuperação, com média de: ",media:2:2)
          senao
               se media < 5 entao
                  escreval("O aluno foi reprovado, com média de: ",media:2:2)
               fimse
          fimse
     fimse

caso 2
     interrompa
outrocaso
         limpatela
         escreval(" Opção invalida ")
         escreval("")
         escreval("")
         fimescolha
ate menu=2

Fimalgoritmo