Algoritmo "trabalho(finall)"
// Disciplina : [Linguagem e Lógica de Programação]
// Professor :
// Descrição :
// Autor(a) : Gabriel Mazzuchello Dal Molin / Danilo Formanski / João Vitor Goulart Viana
// Data atual : 05/10/2021
Var
//Declaração de variaveis
matris: vetor [1..10, 1..3] de caractere
menu, QuantidadeLista, pessoas, listagem, NewQuantidadeLista : inteiro

Inicio
repita
      escreval ("Digite a Quantidade de pessoas que vc deseja(máximo 10)")
      leia (NewQuantidadeLista)
      limpatela

ate NewQuantidadeLista < 11
pessoas <- 0

repita
      escreval("==============================================")
      escrevaL("= Informe uma opção!!                        =")
      escreval("=                                            =")
      escreval("= 1° Cadastro                                =")
      escreval("= 2° Lista                                   =")
      escreval("= 3° Alterar o tamanho da lista              =")
      escreval("= 4° Sair                                    =")
      escreval("==============================================")
      leia(menu)

//Menu de escolhas
escolha(menu)
caso 1
     limpatela
     se pessoas >= 10 entao
          escreval("A lista esta cheia")
          escreval("")
          escreval("")
     senao
          pessoas <- pessoas +1
          escreval ("Digite o nome da ",pessoas,"ª pessoa")
          leia(matris[pessoas,1])
          escreval ("Digite o telefone da ",pessoas,"ª pessoa")
          leia (matris[pessoas,2])
          escreval ("Digite o email da ",pessoas,"ª pessoa")
          leia (matris[pessoas,3])
          limpatela
     fimse

    //Usado para cadastrar as pessoas
caso 2
     limpatela
     se pessoas<=0 entao
        escreval (" Não tem nenhuma pessoa cadastrada")
        escreval ("")
        escreval ("")
     senao
        para listagem de 1 ate pessoas faca
        escreval ("Nome : ",matris[listagem,1])
        escreval ("Telefone : ",matris[listagem,2])
        escreval ("Email : ",matris[listagem,3])
        escreval ("")
        fimpara
     escreval("Digite qualquer coisa para voltar ao menu")
     leia(menu)
     limpatela
     fimse

//Usado para mostrar as pessoas cadastradas

caso 3
     escreval ("Digite a Quantidade de pessoas que vc deseja(máximo 10)")
     leia (NewQuantidadeLista)
     se NewQuantidadeLista > 10 entao
        limpatela
        escreval(" Número invalido ")
        escreval("")
        escreval("")
     senao
        se NewQuantidadeLista > QuantidadeLista entao
        QuantidadeLista <- NewQuantidadeLista
        limpatela
        senao
           limpatela
           escreval(" Número invalido ")
           escreval("")
           escreval("")
        fimse
     fimse

//Usado para determinar a quantidade de cadastro
caso 4
     interrompa

//Para encerrar o programa
outrocaso
         limpatela
         escreval(" Opção invalida ")
         escreval("")
         escreval("")
         //Caso o que foi digitado não corresponder a uma opção valida
       fimescolha
      //Repitir até a escolha sair do programa
      ate menu=4
Fimalgoritmo