import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        self.__Grafo = nx.Graph()

    @property
    def vertices(self):
        return list(self.__Grafo.nodes)

    @property
    def arestas(self):
        return list(self.__Grafo.edges)
    
    def busca_vertices_adjacentes(self, vertice):
        if self.vertice_existe(vertice):
            return list(self.__Grafo.neighbors(vertice))
        else:
            raise ValueError("Vértice não existe.")

    def peso_aresta(self, v1, v2):
        if self.aresta_existe(v1, v2):
            return self.__Grafo[v1][v2]['weight']
        else:
            raise ValueError("Aresta não existe.")

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

    def adiciona_vertice(self, rotulo_vertice):
        if not self.vertice_existe(rotulo_vertice):
            self.__Grafo.add_node(rotulo_vertice)
        else:
            raise ValueError("O vertice já existe.")

    def remove_vertice(self, rotulo_vertice):
        self.__Grafo.remove_node(rotulo_vertice)

    def retorna_vertice(self, rotulo_vertice):
        index = self.vertices.index(rotulo_vertice)
        return self.vertices[index]

    def aresta_existe(self,v1,v2):
        return self.__Grafo.has_edge(v1, v2)

    def vertice_existe(self,v1):
        return self.__Grafo.has_node(v1)

    def mostra_grafo(self):
        pos = nx.spring_layout(self.__Grafo)
        labels = nx.get_edge_attributes(self.__Grafo, 'weight')
        nx.draw(self.__Grafo, pos, with_labels=True)
        nx.draw_networkx_edge_labels(self.__Grafo, pos, edge_labels=labels)
        plt.show()

grafo = Grafo()

grafo.adiciona_vertice("Vila Natal")
grafo.adiciona_vertice("Capão Redondo")
grafo.adiciona_vertice("Santo Amaro")

grafo.adiciona_aresta(grafo.retorna_vertice("Santo Amaro"), grafo.retorna_vertice("Vila Natal"), 6)
grafo.adiciona_aresta(grafo.retorna_vertice("Santo Amaro"), grafo.retorna_vertice("Capão Redondo"), 4)

print(grafo.vertices)
print(grafo.arestas)

grafo.mostra_grafo()