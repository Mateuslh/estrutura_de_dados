import networkx as nx
import matplotlib.pyplot as plt

class DesenhaGrafo:
    
    def __init__(self):
        self.__Grafo = nx.Graph()

    @property
    def vertices(self):
        return list(self.__Grafo.nodes)

    @property
    def arestas(self):
        return list(self.__Grafo.edges)

    def vertice_existe(self,v1):
        return self.__Grafo.has_node(v1)
    
    def aresta_existe(self,v1,v2):
        return self.__Grafo.has_edge(v1, v2)
    
    def adiciona_vertice(self, rotulo_vertice, px, py):
        if not self.vertice_existe(rotulo_vertice):
            self.__Grafo.add_node(rotulo_vertice, pos=(px, py))
        else:
            raise ValueError("O vertice já existe.")
    
    def adiciona_aresta(self, v1, v2, custo):
        if not self.aresta_existe(v1, v2):
            self.__Grafo.add_edge(v1, v2, weight=custo)
        else:
            raise ValueError("A aresta já existe.")
    
    def busca_vertice(self, vertice):
        if self.vertice_existe(vertice):
            return self.vertices[self.vertices.index(vertice)]
        else:
            raise ValueError("Vértice não existe.")
    
    def busca_vertices_adjacentes(self, vertice):
        if self.vertice_existe(vertice):
            return list(self.__Grafo.neighbors(vertice))
        else:
            raise ValueError("Vértice não existe.")

    def remove_vertice(self, rotulo_vertice):
        self.__Grafo.remove_node(rotulo_vertice)

    def remove_aresta(self, v1, v2):
        if self.aresta_existe(v1, v2):
            self.__Grafo.remove_edge(v1, v2)
            return True
        else:
            raise KeyError("Aresta não existe.")

    def mostra_grafo(self):
        pos = nx.get_node_attributes(self.__Grafo, 'pos')
        labels = nx.get_edge_attributes(self.__Grafo, 'weight')
        nx.draw_networkx(self.__Grafo, pos, node_color ="#FFCD00", node_size=750, node_shape='p', width=0.5, font_size=10, font_weight='bold' )
        nx.draw_networkx_edge_labels(self.__Grafo, pos, edge_labels=labels)
        plt.show()
