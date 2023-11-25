class Adjacente:

    def __init__(self, vertice, custo):
        self.__vertice = vertice
        self.__custo = custo

    @property
    def vertice(self):
        return self.__vertice

    @property
    def custo(self):
        return self.__custo
    
    @vertice.setter
    def vertice(self, vertice):
        self.__vertice = vertice

    @custo.setter
    def custo(self, custo):
        self.__custo = custo
