import unittest
from domain.desenha_grafo import DesenhaGrafo

class TestGrafo(unittest.TestCase):
    
    def setUp(self):
        self.arestas_exemplo = [
            ('Arad', 'Zerind', 75),
            ('Arad', 'Sibiu', 140),
            ('Arad', 'Timisoara', 118),
        ]
        self.grafo = DesenhaGrafo()
        self.grafo.mostra_grafo()
    
    def test_adiciona_aresta(self):
        self.grafo.adiciona_aresta('Sibiu', 'Fagaras', 99)
        self.assertTrue(self.grafo.aresta_existe('Sibiu', 'Fagaras'))

    def test_remove_aresta(self):
        self.grafo.mostra_grafo()
        self.assertTrue(self.grafo.remove_aresta('Sibiu', 'Arad'))
        self.assertFalse(self.grafo.aresta_existe('Sibiu', 'Arad'))

    def test_adiciona_vertice(self):
        self.grafo.adiciona_vertice('NewCity')
        self.assertTrue(self.grafo.aresta_existe('NewCity'))

    def test_remove_vertice(self):
        self.grafo.remove_vertice('Sibiu')
        self.assertFalse(self.grafo.aresta_existe('Sibiu'))

if __name__ == '__main__':
    unittest.main()