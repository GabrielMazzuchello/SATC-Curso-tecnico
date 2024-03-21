Algoritmo "ex004 salario liquido"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Gabriel Mazzuchello Dal Molin Turma: 1137
// Data atual  : 21/03/2024
Var
// Seção de Declarações das variáveis
valorhora, horas, ir, inss, sindicato, salario, salariototal : real

Inicio

escreval("informe o valor por hora que você ganha: ")
leia(valorhora)
escreval("Informe quantas horas você trabalhou: ")
leia(horas)


salario <- valorhora * horas

ir <- (salario / 100 * 11)
salariototal <- salario - ir

inss <- (salariototal / 100 * 8)
salariototal <- salariototal - inss

sindicato <- (salariototal / 100 * 5)
salariototal <- salariototal - sindicato



limpatela
escreval("Seu salário bruto é de:",salario)
escreval("Seu Inposto de renda é de: ",ir)
escreval("Seu INSS é de: ",inss)
escreval("Seu sindicato é de: ",sindicato)
escreval("Seu salario líquido é de: ",salariototal)



Fimalgoritmo