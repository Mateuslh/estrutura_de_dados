import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self, arestas):
        self.__Grafo = nx.Graph()

        for aresta in arestas:
            v1, v2, custo = aresta
            self.__Grafo.add_edge(v1, v2, weight=custo)

    def adiciona_aresta(self, v1, v2, custo):
        if not self.aresta_existe(v1, v2):
            self.__Grafo.add_edge(v1, v2, weight=custo)
        else:
            raise ValueError("A aresta já existe.")

    def remove_aresta(self, v1, v2):
        if self.aresta_existe(v1, v2):
            self.__Grafo.remove_edge(v1, v2)
            return True
        else:
            raise KeyError("Aresta não existe.")
            return False

    def adiciona_vertice(self, rotulo_vertice):
        if not self.vertice_existe(rotulo_vertice):
            self.__Grafo.add_node(rotulo_vertice)
        else:
            raise ValueError("O vertice já existe.")

    def remove_vertice(self, rotulo_vertice):
        self.__Grafo.remove_node(rotulo_vertice)

    def aresta_existe(self,v1,v2):
        return self.__Grafo.has_edge(v1, v2)

    def vertice_existe(self,v1):
        return self.__Grafo.has_node(v1)

    def mostra_grafo(self):
        pos = nx.spring_layout(self.__Grafo)  # layout para melhor visualização
        labels = nx.get_edge_attributes(self.__Grafo, 'weight')
        nx.draw(self.__Grafo, pos, with_labels=True)
        nx.draw_networkx_edge_labels(self.__Grafo, pos, edge_labels=labels)
        plt.show()