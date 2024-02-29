Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 29/02/2024
Var
// Seção de Declarações das variáveis 
valorfabrica, distribuicao, valortotal : real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
//  porcentagem do distribuidor seja de 20% e os impostos de 35%,
escreval("Informe o valor de fabrica do veiculo ")
leia(valorfabrica)
limpatela

distribuicao <- valorfabrica * 1.20
valortotal <- distribuicao * 1.35

escreval("O valor total do veiculo é de : ",valortotal)

Fimalgoritmo