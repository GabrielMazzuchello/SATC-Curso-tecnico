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

se (siglacurso = "ADM") ou (siglacurso = "adm") entao
   escreval("Bem vindo! ",nome, " ao curso de Administração")
senao
     se (siglacurso = "DIR") ou (siglacurso = "dir") entao
        escreval("Bem vindo! ",nome, " ao curso de Direito")
     senao
          se (siglacurso = "CEX") ou (siglacurso = "cex") entao
             escreval("Bem vindo! ",nome, " ao curso de Comércio Exterior")
          senao
             escreval("Curso não reconhecido")
             
          fimse
     fimse
fimse

Fimalgoritmo