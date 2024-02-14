import random

class Sorteador:

    def __init__(self):

        # A list containing pre-established words grouped by classification: fruits and school/office materials.
        self.opcoes_palavras = ["banana", "maça", "pera", "abacaxi", "abacate", "melancia", "laranja", "caneta", "lapis",
                              "borracha", "estojo", "lapizeira","casa","cama","microondas","cozinha","computador","mesa","copo",
                              "tomada","ponte","chinelo","cortina","janela","escrivaninha","porta","celular","colher","garfo","faca",
                              "pente","esparadrafo","cobertor","travesseiro","cachorro","gato","rato","coelho","cocrodilo","pinguim","baleia"
                            "cidade","estado","van","estrada","rodovia","metro","violino","violancelo","lua","sol","mercurio","venus"
                              ,"marte","jupiter","neturno","saturno","urano","plutao","estrela","capa","luz","materia","folha","agua","fogo"
                            ,"metal","jornal",""]

        # Save the drawn word
        self.palavra_sorteada = self.sortear_palavra()

    # Do the strength's draw
    def sortear_palavra(self):
        return random.choice(self.opcoes_palavras)