Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 14/03/2024
Var
// Seção de Declarações das variáveis 
nome, estadocivil : caractere

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("Informe seu nome: ")
leia(nome)
escreval("Informe seu estado civil: ")
leia(estadocivil)

escolha(estadocivil)

caso "S"
     escreval(nome, " voce está solteiro(a)")
caso "C"
     escreval(nome, " voce está casado(a)")
caso "V"
     escreval(nome, " voce está viuvo(a)")
caso "D"
     escreval(nome, " voce está divorciado")
outrocaso
     escreval("Opção invalida, tente novamente")
fimescolha


Fimalgoritmo