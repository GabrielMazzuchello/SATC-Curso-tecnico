import random

def desenhar_forca(erro):
    estagios = [
        """
           -----
           |   |
               |
               |
               |
               |
         ______|__
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
         ______|__
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
         ______|__
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
         ______|__
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
         ______|__
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
         ______|__
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
         ______|__
        """
    ]
    print(estagios[erro])

palavras_secretas = ['python', 'programação', 'computador','algoritmo']
letras_adivinhadas = []
letras_corretas = []
n_letras = []

palavra_escolhida = random.choice(palavras_secretas)

vida = 6
erro = 0

numero_letras = len(palavra_escolhida)
for c in range(numero_letras):
    n_letras.append('_')

while True:
    print(" ".join(n_letras))
    print(desenhar_forca(erro))
    if vida != 0:

        letra_a_verificar = input("Informe uma letra: ").lower().strip()
        print('')

        for c in palavra_escolhida:
            if c in letra_a_verificar:
                index = palavra_escolhida.index(c)
                n_letras[index] = letra_a_verificar


        if letra_a_verificar in palavra_escolhida:
            letras_corretas.append(letra_a_verificar)
            letras_adivinhadas.append(letra_a_verificar)
            print('letra correta!')
            print('')

            print('Letras corretas: ')
            print((" ".join(letras_corretas)))
            print('')
            print('Letras adivinhadas: ')
            print((" ".join(letras_adivinhadas)))

            print(" ".join(n_letras))

            escolha = str(input('Você desejá tentar adivinhar a palavra? (S/N)')).upper().strip()
            if escolha == 'S':
                print('')
                palavra = input('Informe a palavra: ').lower().strip()
                print('')
                if palavra == palavra_escolhida:
                    print('Voce acertou parabens!!')
                    break
                else:
                    print('Você errou! continue tentando')
            else:
                print('Então continue tentando adivinhar as letras!')
                print('')
        else:
            letras_adivinhadas.append(letra_a_verificar)
            vida -= 1
            print('Letra errada!')
            print('Suas vidas {}'.format(vida))
            print('')
            erro += 1
    else:
        print('Voce perdeu!!!')
        print('A palavra era {}'.format(palavra_escolhida))
        break


        
