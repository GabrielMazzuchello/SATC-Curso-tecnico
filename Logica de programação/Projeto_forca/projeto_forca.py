import random

palavras_secretas = ['python', 'programação', 'computador','algoritmo']
letras_adivinhadas = []
letras_corretas = []

palavra_escolhida = random.choice(palavras_secretas)

vida = 6

while True:
    if vida != 0:
        letra_a_verificar = str(input("Informe uma letra: ")).lower().strip()

        if letra_a_verificar in palavra_escolhida:
            letras_corretas.append(letra_a_verificar)
            letras_adivinhadas.append(letra_a_verificar)
            print('letra correta!')

            for c in letras_corretas:
                print('Letras corretas: {}'.format(c))

            escolha = str(input('Você desejá tentar adivinhar a palavra? (S/N)')).upper().strip()
            if escolha == 'S':
                palavra = str(input('Informe a palavra: ')).lower().strip()
                if palavra == palavra_escolhida:
                    print('Voce acertou parabens!!')
                    break
                else:
                    print('Você errou! continue tentando')
            else:
                print('Então continue tentando adivinhar as letras!')
        else:
            letras_adivinhadas.append(letra_a_verificar)
            vida -= 1
            print('Letra errada!')
    else:
        print('Voce pereu!!!')
        break


        
