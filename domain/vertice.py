from adjacente import Adjacente

class Vertice:

    def __init__(self, rotulo):
        self.__rotulo = rotulo
        self.__adjacentes = []

    @property 
    def rotulo(self):
        return self.__rotulo

    @property
    def adjacentes(self):
        return self.__adjacentes
    
    @rotulo.setter
    def rotulo(self, rotulo):
        self.__rotulo = rotulo

    def adicionar_adjacente(self, vertice, custo):
        self.adjacentes.append(Adjacente(vertice, custo))

    def retornar_adjacente(self, vertice):
        for adjacente in self.adjacentes:
            if (adjacente.vertice == vertice):
                return adjacente.vertice.rotulo

    def mostra_adjacentes(self):
        for adjacente in self.adjacentes:
            print(f'Vertice: {adjacente.vertice.rotulo} - Custo: {adjacente.custo}')

