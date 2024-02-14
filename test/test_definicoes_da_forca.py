from forca.definicoes_da_forca import Forca
import unittest

class TestClasse(unittest.TestCase):

    def setUp(self):
        self.test_forca = Forca()

    def test_desenho_da_forca(self):
        self.assertEqual(len(self.test_forca.quant_lacunas),len(self.test_forca.sorteador.palavra_sorteada))

    def test_layout_da_froca(self):
        pass

    def test_apuracao_da_forca(self):
        pass

if __name__ == '__main__':
    unittest.main()
