Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 14/03/2024
Var
// Se��o de Declara��es das vari�veis 
nome, siglacurso, curso : caractere

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
escreval("informe seu nome: ")
leia(nome)
escreval("Informe a sigla do seu curso (ADM, DIR, CEX): ")
leia(siglacurso)
limpatela

se (siglacurso = "ADM") ou (siglacurso = "adm") entao
   escreval("Bem vindo! ",nome, " ao curso de Administra��o")
senao
     se (siglacurso = "DIR") ou (siglacurso = "dir") entao
        escreval("Bem vindo! ",nome, " ao curso de Direito")
     senao
          se (siglacurso = "CEX") ou (siglacurso = "cex") entao
             escreval("Bem vindo! ",nome, " ao curso de Com�rcio Exterior")
          senao
             escreval("Curso n�o reconhecido")
             
          fimse
     fimse
fimse

Fimalgoritmo