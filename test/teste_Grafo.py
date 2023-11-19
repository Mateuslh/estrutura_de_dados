import unittest
from domain.Grafo import Grafo
class TestGrafo(unittest.TestCase):
    def setUp(self):
        self.arestas_exemplo = [
            ('Arad', 'Zerind', 75),
            ('Arad', 'Sibiu', 140),
            ('Arad', 'Timisoara', 118),
        ]
        self.grafo = Grafo(self.arestas_exemplo)

    def test_adiciona_aresta(self):
        self.grafo.adiciona_aresta('Sibiu', 'Fagaras', 99)
        self.assertTrue(self.grafo.__Grafo.has_edge('Sibiu', 'Fagaras'))

    def test_remove_aresta(self):
        self.assertTrue(self.grafo.remove_aresta('Sibiu', 'Arad'))
        self.assertFalse(self.grafo.__Grafo.has_edge('Sibiu', 'Arad'))

    def test_adiciona_vertice(self):
        self.grafo.adiciona_vertice('NewCity')
        self.assertTrue(self.grafo.__Grafo.has_node('NewCity'))

    def test_remove_vertice(self):
        self.grafo.remove_vertice('Sibiu')
        self.assertFalse(self.grafo.__Grafo.has_node('Sibiu'))

if __name__ == '__main__':
    unittest.main()