Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 29/02/2024
Var
// Se��o de Declara��es das vari�veis 
valorfabrica, distribuicao, valortotal : real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc...
//  porcentagem do distribuidor seja de 20% e os impostos de 35%,
escreval("Informe o valor de fabrica do veiculo ")
leia(valorfabrica)
limpatela

distribuicao <- valorfabrica * 1.20
valortotal <- distribuicao * 1.35

escreval("O valor total do veiculo � de : ",valortotal)

Fimalgoritmo