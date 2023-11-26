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

    def adjacente_existe(self, vertice):
        for adjacente in self.__adjacentes:
            if (adjacente.vertice == vertice):
                return True
        return False

    def adicionar_adjacente(self, vertice, custo):
        if not self.adjacente_existe(vertice):
            self.__adjacentes.append(Adjacente(vertice, custo))
            return True
        else:
            return False
        
    def remover_adjacente(self, vertice):
        for adjacente in self.__adjacentes:
            if (adjacente.vertice == vertice):
                self.__adjacentes.remove(adjacente)
                return True
        return False
    
    def buscar_adjacente(self, vertice):
        for adjacente in self.__adjacentes:
            if (adjacente.vertice == vertice):
                return adjacente.vertice
        return False

    def mostra_adjacentes(self):
        for adjacente in self.__adjacentes:
            print(f'Vertice: {adjacente.vertice.rotulo} - Custo: {adjacente.custo}')

    
    


