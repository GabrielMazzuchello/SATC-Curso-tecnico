Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 14/03/2024
Var
// Se��o de Declara��es das vari�veis 
nome, estadocivil : caractere

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("Informe seu nome: ")
leia(nome)
escreval("Informe seu estado civil: ")
leia(estadocivil)

escolha(estadocivil)

caso "S"
     escreval(nome, " voce est� solteiro(a)")
caso "C"
     escreval(nome, " voce est� casado(a)")
caso "V"
     escreval(nome, " voce est� viuvo(a)")
caso "D"
     escreval(nome, " voce est� divorciado")
outrocaso
     escreval("Op��o invalida, tente novamente")
fimescolha


Fimalgoritmo