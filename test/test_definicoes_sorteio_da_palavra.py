from sorteio_palavra.definicoes_sorteio_da_palavra import Sorteador
import unittest

class TestDefinicoesSorteioDaPalavra(unittest.TestCase):

    def setUp(self):

        self.test_sorteador = Sorteador()
        self.test_opcoes_palavras = self.test_sorteador.opcoes_palavras

    def test_sortear_palavra(self):

        self.assertIn(self.test_sorteador.palavra_sorteada, self.test_opcoes_palavras)

if __name__ == '__main__':
    unittest.main()
