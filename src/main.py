"""
This module implements a simple hangman game and related utility functions.
"""

from forca.definicoes_da_forca import Forca
import os

def limpador(booleano):
    """
    Clears the console screen based on the operating system.

    Parameters:
    - booleano (bool): A boolean value indicating whether to pause after clearing the screen.
    """
    if booleano:
        input('Precione ENTER para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

def impressao_mensagem_fim_de_jogo(resultado_acertou, resultado_enforcou, a_palavra_secreta):
    """
    Prints the end-of-game message based on the game result.

    Parameters:
    - resultado_acertou (bool): Indicates whether the player won the game.
    - resultado_enforcou (bool): Indicates whether the player lost the game.
    - a_palavra_secreta (str): The secret word for the game.
    """
    limpador(False)

    if resultado_acertou:
        print('Parabéns! Você ganhou!\n')
        print(r"       ___________      ")
        print(r"      '._==_==_=_.'     ")
        print(r"      .-\\:      /-.    ")
        print(r"     | (|:.     |) |    ")
        print(r"      '-|:.     |-'     ")
        print(r"        \\::.    /      ")
        print(r"         '::. .'        ")
        print(r"           ) (          ")
        print(r"         _.' '._        ")
        print("         '-------'       \n")
            
    elif resultado_enforcou:
        print('Puxa, você foi enforcado!  \n')
        print(r"    _______________         ")
        print(r"   /               \        ")
        print(r"  /                 \       ")
        print(r"//                   \/\    ")
        print(r"\|   XXXX     XXXX   | /    ")
        print(r" |   XXXX     XXXX   |/     ")
        print(r" |   XXX       XXX   |      ")
        print(r" |                   |      ")
        print(r" \__      XXX      __/      ")
        print(r"   |\     XXX     /|        ")
        print(r"   | |           | |        ")
        print(r"   | I I I I I I I |        ")
        print(r"   |  I I I I I I  |        ")
        print(r"   \_             _/        ")
        print(r"     \_         _/          ")
        print(r"       \_______/             ")
        print('')
        print(f'A palavra era {a_palavra_secreta} \n')

def main():
    """
    Main function to execute the hangman game.
    """
    # Clear the console
    limpador(False)

    # Game introduction
    print('***************************************************************')
    print('*************** Bem-vindo ao jogo-da-forca ********************')
    print('***************************************************************\n')

    # Update game stages
    limpador(True)

    # Game rules presentation
    print('*********************** Regras do jogo ****************************')

    # Clarifying the rules of the game
    print('Como funciona?\n')
    print('O jogo da forca consiste em adivinhar uma palavra escolhida aleatoriamente.')
    print('Você só pode tentar adivinhar por 7 tentativas escolhendo letras.')
    print('As letras corretamente adivinhadas serão integradas à forca, da qual você deve adivinhar a palavra para vencer o jogo.\n')
    print('ATENÇÃO!!!!!')
    print('Você perde se fizer um total de 7 palpites errados.\n')
    print('DIVIRTA-SE :) !!\n')

    # Update game stages
    limpador(True)

    # Game logic loop
    while True:
        # Set up hangman
        forca = Forca()

        # Flags for game status
        acertou, enforcou = False, False

        while not acertou and not enforcou:
            # Clear the console
            limpador(False)

            # Display hangman and related information
            forca.layout_forca()

            # Player's guess
            chute = input('What is your guess?\n')

            # Check if the guess corresponds to any letter in the word
            forca.apuracao_da_forca(chute)

            # Check win or lose conditions
            acertou = '_' not in forca.quant_lacunas
            enforcou = forca.erros == 7

        # Print end-of-game message
        impressao_mensagem_fim_de_jogo(acertou, enforcou, forca.sorteador.palavra_sorteada)

        # Update game stages
        limpador(True)

        # Check if the player wants to play again
        jogar_denovo = input('Desseja jogar novamente?? (s/n):\n')

        # If not, end the game
        if jogar_denovo != 's':
            break

            # Clear the console
            limpador(False)
            print('Obrigado por jogar ;)')

if __name__ == '__main__':
    main()

