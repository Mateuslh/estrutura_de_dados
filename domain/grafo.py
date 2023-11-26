from vertice import Vertice

class Grafo:

    def __init__(self, rotulo_grafo):
        self.__rotulo_grafo = rotulo_grafo
        self.__vertices = []

    @property
    def rotulo_grafo(self):
        return self.__rotulo_grafo

    @property
    def vertices(self):
        return self.__vertices
    
    @rotulo_grafo.setter
    def rotulo_grafo(self, rotulo_grafo):
        self.__rotulo_grafo = rotulo_grafo
    
    def vertice_existe(self, rotulo_vertice):
        for vertice in self.__vertices:
            if (vertice.rotulo_vertice == rotulo_vertice):
                return True
        return False

    def adiciona_vertice(self, rotulo_vertice):
        if not self.vertice_existe(rotulo_vertice):
            novo_vertice = Vertice(rotulo_vertice)
            self.__vertices.append(novo_vertice)
            return novo_vertice
        else:
            return False
    
    def remove_vertice(self, vertice):
        for vertice_grafo in self.__vertices:
            if (vertice_grafo == vertice):
                self.__vertices.remove(vertice_grafo)
                return True
        return False

    def busca_vertice(self, vertice):
        for vertice_grafo in self.__vertices:
            if (vertice_grafo == vertice):
                return vertice_grafo
        return False

    def mostra_vertices(self):
        for vertice_grafo in self.__vertices:
            print(f'Vértice: {vertice_grafo.rotulo_vertice}')
            vertice_grafo.mostra_adjacentes()




    

    
