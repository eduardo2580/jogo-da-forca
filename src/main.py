from forca.definicoes_da_forca import Forca
import os
        
def limpador(booleano):

    if (booleano):
        input('Precione ENTER para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

def impressao_mensagem_fim_de_jogo(resultado_acertou, resultado_enforcou, a_palavra_secreta):

    limpador(False)

    if (resultado_acertou):

        print('Parabéns, você ganhou! \n')
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

    elif (resultado_enforcou):

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

    # Clear the content given above
    limpador(False)

    # Hangman game presentation
    print('***************************************************************')
    print('*************** Bem-Vindo ao jogo da forca ********************')
    print('*************************************************************** \n')

    # Updating game stages
    limpador(True)

    # Presentation of the game rules
    print('*********************** Regras do Jogo ****************************')

    # Clarifying the rules of the game, how it will work.
    print('Como funciona?? \n')
    print(
        'O jogo da forca consiste em adivinha uma palavra sorteada. Você só poderá tentar adivinha por \n tentativas, chutando letras a sua escolha.')
    print('As letras acertadas seram integradas á forca, da qual você deve acerta a palavra para ganhar o jogo. \n')
    print('ATENÇÃO!!!!!')
    print('Você perde se errar um total de 7 chutes. \n')
    print('BOM JOGO :) !! \n')

    # Updating game stages
    limpador(True)

    # Game logic
    while True:

        # Strength
        forca = Forca()

        # loop validation variables
        acertou, enforcou = False, False

        while (not acertou and not enforcou):
            # Clears previously displayed content
            limpador(False)

            # Gallows display and relevant information
            forca.layout_forca()

            # Player shot capture
            chute = input('Qual é o seu chute? \n')

            # Determines if the guess corresponds to any letter in the word
            forca.apuracao_da_forca(chute)

            # Conditions for losing or winning the game
            acertou = '_' not in forca.quant_lacunas
            enforcou = forca.erros == 7

        # Printing the end of game message
        impressao_mensagem_fim_de_jogo(acertou, enforcou, forca.sorteador.palavra_sorteada)

        # Updating game stages
        limpador(True)

        # Checks whether the player who plays again
        jogar_denovo = input('Deseja jogar novamente?? (s/n): \n')

        # If not, end the game
        if jogar_denovo != 's':
            break

            # Clears previously displayed content
            limpador(False)
            print('Obrigado por jogar ;)')

if __name__ == '__main__':
    main()
