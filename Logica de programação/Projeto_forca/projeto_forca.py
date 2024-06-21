# Importa o módulo random para selecionar uma palavra aleatória
import random

def desenhar_forca(erro):
    # Estagios da forca, dependendo da quantidade deerro
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
    # Mostra ao ussuario o  estagio da forca
    print(estagios[erro])

palavras_secretas = ['python', 'programação', 'computador', 'algoritmo'] # Lista de palavras para o jogo
letras_adivinhadas = [] # Lista para armazenar todas as letras que foram informadas
letras_corretas = [] # Lista para armazenar as letras corretas
n_letras = [] # Lista para mostrar a palavra com as letras adivinhadas e as que ainda não foram fica com um espaço

palavra_escolhida = random.choice(palavras_secretas) # Escolhe aleatoriamente uma palavra da lista

vida = 6 # numero de vidas e de erros
erro = 0

# caucula a quantidade de letras que a palavra escolhida tem e cria a lista com o numero de letras da palavra
numero_letras = len(palavra_escolhida)
for c in range(numero_letras):
    n_letras.append('_')

# Loop principal do jogo
while True:
    print('Dica: Relacionado ao curso')
    print("Palavra: ", " ".join(n_letras)) # Mostra a palavra com as letras adivinhadas e as que não foram ficam com uma underline
    desenhar_forca(erro) # Desenha a forca 
    
    # verifica sua vida, se for 0 o jogador perde
    if vida == 0:
        print('Você perdeu!!!')
        print('A palavra era {}'.format(palavra_escolhida))
        break
    try:
        # Pede uma letra do jogador
        letra_a_verificar = input("Informe uma letra: ").lower().strip()

        if not letra_a_verificar.isalpha():
            # Verifica se foi informado algo alem de uma letra, retorna um erro
            raise ValueError('Entrada inválida: Apenas letras são permitidas.')
    
        if letra_a_verificar in letras_adivinhadas:
            # Verifica se a letra já foi adivinhada antes, pede outra letra
            print('Você já tentou essa letra. Tente outra.')
            continue
        
        # Adiciona a letra adivinhada à lista de letras adivinhadas
        letras_adivinhadas.append(letra_a_verificar)
        
        if letra_a_verificar in palavra_escolhida:
            # Verifica se a letra está na palavra escolhida
            print('Letra correta!\n')
            letras_corretas.append(letra_a_verificar)

            # Atualiza a lista n_letras para mostrar a letra nas posições certas
            for idx, letra in enumerate(palavra_escolhida):
                if letra == letra_a_verificar:
                    n_letras[idx] = letra

            # Verifica se todas as letras foram adivinhadas, se sim o jogador vence
            if '_' not in n_letras:
                print('Parabéns! Você adivinhou a palavra: {}'.format(palavra_escolhida))
                break

        # Verifica se a letra não está na palavra escolhida, e retorna uma adivinhação errada
        else:
            print('Letra errada!')
            vida -= 1 # Reduz uma vida e almenta um erro
            erro += 1
            print('Suas vidas: {}'.format(vida))
        
        # Mostra as letras corretas e adivinhadas até o momento
        print('Letras corretas: ', " ".join(letras_corretas))
        print('Letras adivinhadas: ', " ".join(letras_adivinhadas))
        print()
        print(" ".join(n_letras)) # Mostra a palavra atualizada com as letras adivinhadas para o jogador escoher tentar ou não adivinhar
        
        # Pergunta ao jogador se ele deseja tentar adivinhar a palavra
        escolha = input('Você deseja tentar adivinhar a palavra? (S/N) ').upper().strip()
        if escolha == 'S':
            palavra = input('Informe a palavra: ').lower().strip()
            if palavra == palavra_escolhida:
                # Se a palavra estiver correta, o jogador vence
                print('Você acertou, parabéns!!')
                break
            else:
                # Se a palavra estiver errada, pede para continuar tentando (Não a penaidade por errar)
                print('Você errou! Continue tentando.')
    except ValueError as ve:
        # Mostra a mensagem de erro para entradas inválidas da verificação da linha 105
        print(ve)

# mensagem informando que o jogo acabou
print('Fim do jogo.')
