Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 14/03/2024
Var
// Seção de Declarações das variáveis 
nome, siglacurso, curso : caractere

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
escreval("informe seu nome: ")
leia(nome)
escreval("Informe a sigla do seu curso (ADM, DIR, CEX): ")
leia(siglacurso)
limpatela

se siglacurso = "ADM" entao
   escreval("Bem vindo! ",nome, " ao curso de Administração")
fimse

se siglacurso = "DIR" entao
   escreval("Bem vindo! ",nome, " ao curso de Direito")
fimse

se siglacurso = "CEX" entao
   escreval("Bem vindo! ",nome, " ao curso de Comércio Exterior")
fimse

Fimalgoritmo