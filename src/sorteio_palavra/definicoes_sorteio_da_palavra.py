import random

class Sorteador:
    """
    Class to manage the drawing of words for the hangman game.
    """

    def __init__(self):
        """
        Initializes a new instance of the Sorteador class.

        It initializes a list containing pre-established words grouped by classification.
        It saves the drawn word.
        """

        self.opcoes_palavras = [
            "banana", "maça", "pera", "abacaxi", "abacate", "melancia", "laranja", "caneta", "lapis",
            "borracha", "estojo", "lapizeira", "casa", "cama", "microondas", "cozinha", "computador", "mesa", "copo",
            "tomada", "ponte", "chinelo", "cortina", "janela", "escrivaninha", "porta", "celular", "colher", "garfo",
            "faca", "pente", "esparadrafo", "cobertor", "travesseiro", "cachorro", "gato", "rato", "coelho", "cocrodilo",
            "pinguim", "baleia", "cidade", "estado", "van", "estrada", "rodovia", "metro", "violino", "violancelo", "lua",
            "sol", "mercurio", "venus", "marte", "jupiter", "neturno", "saturno", "urano", "plutao", "estrela", "capa",
            "luz", "materia", "folha", "agua", "fogo", "metal", "jornal"
        ]

        self.palavra_sorteada = self.sortear_palavra()  # Save the drawn word

    def sortear_palavra(self):
        """
        Randomly selects a word from the list of word options.

        Returns:
        - palavra_sorteada (str): The randomly chosen word.
        """
        return random.choice(self.opcoes_palavras)
