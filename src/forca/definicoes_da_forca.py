from requisicao_dicionario_aberto.requisicao_dicionario_aberto import requisicao_dicionario_aberto


class Forca:
    """
    Represents a hangman game.
    """

    def __init__(self):
        """
        Initializes a new instance of the Forca class.

        It initializes the Sorteador instance, appends the return of desenho_forca() to a variable,
        initializes the error counter, and keeps track of the letters declared by the player.
        """

        self.palavra_sorteada = requisicao_dicionario_aberto()  # random word
        self.quant_lacunas = self.desenho_forca()  # Appends the return of desenho_forca() to a variable
        self.erros = 0  # Error counter
        self.letras_digitadas = []  # Letters that were declared by the player

    def desenho_forca(self):
        """
        Determines the number of gaps that represent the secret word on the gallows.

        Returns:
        - quant_lacunas (list): A list representing the gaps in the secret word.
        """
        if self.palavra_sorteada is None:
            raise ValueError("A palavra sorteada não foi definida.")

        quant_lacunas = []
        for lacuna in self.palavra_sorteada:
            quant_lacunas.append('_')

        return quant_lacunas

    def layout_forca(self):
        """
        Displays the interactive part of the game: mistakes, kicks, and the secret word.
        """
        print(f'erros: {self.erros}', end=" ")
        print(f'           letras: {self.letras_digitadas} \n')
        print(f'Forca: {self.quant_lacunas} \n')

    def apuracao_da_forca(self, chute: str):
        """
        Finds out if the guess corresponds to any letter of the secret word,
        and if so, replaces it. Otherwise, increments the error counter.

        Parameters:
        - chute (str): The letter guessed by the player.
        """
        if chute in self.palavra_sorteada:
            posicao = 0
            for letras in self.palavra_sorteada:
                if letras == chute:
                    self.quant_lacunas[posicao] = letras
                posicao += 1
        else:
            self.erros += 1

        self.letras_digitadas.append(chute)
