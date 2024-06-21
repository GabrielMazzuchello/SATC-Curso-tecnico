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

palavras_secretas = ['python', 'programação', 'computador', 'algoritmo']
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
    print("Palavra: ", " ".join(n_letras))
    desenhar_forca(erro)
    
    if vida == 0:
        print('Você perdeu!!!')
        print('A palavra era {}'.format(palavra_escolhida))
        break

    letra_a_verificar = input("Informe uma letra: ").lower().strip()
    
    if letra_a_verificar in letras_adivinhadas:
        print('Você já tentou essa letra. Tente outra.')
        continue

    letras_adivinhadas.append(letra_a_verificar)
    
    if letra_a_verificar in palavra_escolhida:
        print('Letra correta!\n')
        for idx, letra in enumerate(palavra_escolhida):
            if letra == letra_a_verificar:
                n_letras[idx] = letra

        if '_' not in n_letras:
            print('Parabéns! Você adivinhou a palavra:', palavra_escolhida)
            break

        letras_corretas.append(letra_a_verificar)
        
    else:
        print('Letra errada!')
        vida -= 1
        erro += 1
        print('Suas vidas: {}'.format(vida))
    
    print('Letras corretas: ', " ".join(letras_corretas))
    print('Letras adivinhadas: ', " ".join(letras_adivinhadas))
    print()
    
    escolha = input('Você deseja tentar adivinhar a palavra? (S/N) ').upper().strip()
    if escolha == 'S':
        palavra = input('Informe a palavra: ').lower().strip()
        if palavra == palavra_escolhida:
            print('Você acertou, parabéns!!')
            break
        else:
            print('Você errou! Continue tentando.')

print('Fim do jogo.')
