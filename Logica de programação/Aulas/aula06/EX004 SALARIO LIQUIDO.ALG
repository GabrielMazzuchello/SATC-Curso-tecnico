Algoritmo "ex004 salario liquido"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Gabriel Mazzuchello Dal Molin Turma: 1137
// Data atual  : 21/03/2024
Var
// Se��o de Declara��es das vari�veis
valorhora, horas, ir, inss, sindicato, salario, salariototal : real

Inicio

escreval("informe o valor por hora que voc� ganha: ")
leia(valorhora)
escreval("Informe quantas horas voc� trabalhou: ")
leia(horas)


salario <- valorhora * horas

ir <- (salario / 100 * 11)
salariototal <- salario - ir

inss <- (salariototal / 100 * 8)
salariototal <- salariototal - inss

sindicato <- (salariototal / 100 * 5)
salariototal <- salariototal - sindicato



limpatela
escreval("Seu sal�rio bruto � de:",salario)
escreval("Seu Inposto de renda � de: ",ir)
escreval("Seu INSS � de: ",inss)
escreval("Seu sindicato � de: ",sindicato)
escreval("Seu salario l�quido � de: ",salariototal)



Fimalgoritmo