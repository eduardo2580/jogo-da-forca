from sorteio_palavra.definicoes_sorteio_da_palavra import Sorteador
class Forca:

    def __init__(self):

        # Instance of Sorteador() in Forca()
        self.sorteador = Sorteador()

        # Appends the return of desenho_forca() to a variable
        self.quant_lacunas = self.desenho_forca()

        # Error counter
        self.erros = 0

        # Letters that were declared by the player
        self.letras_digitadas = []

    # Determines the number of gaps that represented the secret word on the gallows
    def desenho_forca(self):

        quant_lacunas = []
        for lacunas in self.sorteador.palavra_sorteada:
            quant_lacunas.append('_')

        return quant_lacunas

    # Displays the interactive part of the game: mistakes, kicks and the secret word
    def layout_forca(self):

        print(f'erros: {self.erros}', end=" ")
        print(f'           letras: {self.letras_digitadas} \n')
        print(f'Forca: {self.quant_lacunas} \n')

    # Find out if the guess corresponds to any letter of the secret word, and if so, replace it
    def apuracao_da_forca(self, chute):

        if (chute in self.sorteador.palavra_sorteada):

            posicao = 0
            for letras in self.sorteador.palavra_sorteada:

                if letras == chute:
                    self.quant_lacunas[posicao] = letras
                posicao += 1
        else:
            self.erros += 1

        self.letras_digitadas.append(chute)