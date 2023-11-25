from copy import deepcopy
from time import time as tempo

"""
    :notify Funções recursivas possuem a função 'mãe' tendo em vista que precisa ser contabilizado o tempo total da alt-
    eração. 
"""
class Ordenador:

    def __init__(self, registros):
        """
        :param registros: Lista de registros do tipo Number que serão ordernados.
        :return None.
        """
        self.registros = registros

    @property
    def registros(self):
        return self.__list

    @registros.setter
    def registros(self,registros):
        """
        :param registros: registros a serem ordenados.
        :return: None
        """
        if not all(isinstance(elemento, (int, float)) for elemento in registros):
            raise ValueError('A propriedade registros deve receber List<Number>')
        self.__list = registros


    class Retorno:
        def __init__(self,time ,returns):
            """
            Retorno das funções de ordenação
            :param time: tempo da execução
            :param returns: retornos
            """

            self.__time = time
            self.__returns = returns

        def __str__(self):
            return str(self.__returns.join(","))

        @property
        def retorno(self):
            return self.__returns

        @property
        def tempo_execucao(self):
            return self.__time

    def __tempo_ordenacao(self):
        def wrapper(*args, **kwargs):
            """
            Verifica o tempo de execução e executa a função.
            :param args:
            :param kwargs:
            :return: Class<Retorno>
            """
            tempo_inicio = tempo()
            retorno = self(*args, **kwargs)
            tempo_fim = tempo()
            tempo_decorrido = tempo_fim - tempo_inicio
            resultado = Ordenador.Retorno(time= tempo_decorrido, returns= retorno)
            return resultado

        return wrapper

    @staticmethod
    def __inverter_elemento(lista, indice1, indice2):
        """
        Inverte elementos de uma lista.
        :param lista: List<> a ter seus itens alterados.
        :param indice1: Interger do item que ira para a posicao do indice 2.
        :param indice2: Interger do item que ira para a posicao do indice 1.
        :return:
        """
        resultado = lista
        resultado[indice1], resultado[indice2] = resultado[indice2], resultado[indice1]
        return resultado

    @__tempo_ordenacao
    def bubble_sort(self) -> list:
        """
        Percorre os elementos ordenando eles em um grande laço de repetição, diminuindo o range total a cada laço de
        repetição do indice_passagem.
        :rtype:List<Number>.
        :return: Lista ordenada.
        """
        minha_lista = deepcopy(self.__list)
        tamanho_lista = len(self.__list)
        for indice_passagem in range(tamanho_lista):
            for indice_atual in range(0, tamanho_lista - indice_passagem - 1):
                if minha_lista[indice_atual] > minha_lista[indice_atual + 1]:
                    self.__inverter_elemento(minha_lista, indice_atual, indice_atual + 1)
        return minha_lista

    @__tempo_ordenacao
    def insertion_sort(self) -> list:
        """
        Percorre os elementos ordenando eles em um grande laço de repetição, e verifica todos os elementos anteriores
        ou até encontrar um elemento com valor menor que o elemento percorrido.
        :rtype:List<Number>.
        :return: Lista ordenada.
        """
        minha_lista = deepcopy(self.__list)
        tamanho_lista = len(minha_lista)
        for indice_atual in range(1, tamanho_lista):
            elemento_atual = minha_lista[indice_atual]
            indice_anterior = indice_atual - 1
            while indice_anterior >= 0 and elemento_atual < minha_lista[indice_anterior]:
                minha_lista[indice_anterior + 1] = minha_lista[indice_anterior]
                indice_anterior -= 1
            minha_lista[indice_anterior + 1] = elemento_atual
        return minha_lista


    def __merge_sort(self,lista):
        """
        Função que ordena uma lista usando o algoritmo Merge Sort.
        :param lista: Lista a ser ordenada.
        :return: Lista ordenada.
        :rtype:List<Number>.
        """
        if len(lista) > 1:
            meio = len(lista) // 2
            lista_esquerda = lista[:meio]
            lista_direita = lista[meio:]

            self.__merge_sort(lista_esquerda)
            self.__merge_sort(lista_direita)

            indice_esquerda = indice_direita = indice_lista = 0

            while indice_esquerda < len(lista_esquerda) and indice_direita < len(lista_direita):
                if lista_esquerda[indice_esquerda] < lista_direita[indice_direita]:
                    lista[indice_lista] = lista_esquerda[indice_esquerda]
                    indice_esquerda += 1
                else:
                    lista[indice_lista] = lista_direita[indice_direita]
                    indice_direita += 1
                indice_lista += 1

            while indice_esquerda < len(lista_esquerda):
                lista[indice_lista] = lista_esquerda[indice_esquerda]
                indice_esquerda += 1
                indice_lista += 1

            while indice_direita < len(lista_direita):
                lista[indice_lista] = lista_direita[indice_direita]
                indice_direita += 1
                indice_lista += 1
            return lista

    @__tempo_ordenacao
    def merge_sort(self):
        """
        Divide repetidamente a lista em sublistas menores até que cada sublista contenha um único elemento. Em seguida,
        combina essas sublistas em ordem crescente, fundindo-as progressivamente até que a lista original esteja
        completamente ordenada.

        Para ordenar uma lista, o algoritmo Merge Sort realiza os seguintes passos:
        1. Divide a lista não ordenada em duas metades.
        2. Chama recursivamente a função `merge_sort` para cada metade.
        3. Combina (merge) as sublistas ordenadas para criar uma lista ordenada.
        :return: Lista ordenada.
        :rtype:List<Number>.
        """
        minha_lista = deepcopy(self.__list)
        return self.__merge_sort(minha_lista)


    def __quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivô = arr[0]
        menores_ou_iguais = []
        for elemento in arr[1:]:
            if elemento <= pivô:
                menores_ou_iguais.append(elemento)

        maiores = []
        for elemento in arr[1:]:
            if elemento > pivô:
                maiores.append(elemento)
        lista_ordenada = self.__quick_sort(menores_ou_iguais) + [pivô] + self.__quick_sort(maiores)
        return lista_ordenada

    @__tempo_ordenacao
    def quick_sort(self):
        """
           Ordena a lista utilizando o algoritmo Quick Sort, que segue os seguintes passos:
           1. Escolhe um elemento como pivô (geralmente o primeiro elemento).
           2. Particiona a lista em elementos menores ou iguais ao pivô e elementos maiores que o pivô.
           3. Chama recursivamente a função `quick_sort` nas sublistas menores e maiores.
           4. Combina as sublistas ordenadas, colocando o pivô entre elas.

           Repetindo o processo até que cada sublista contenha um único elemento. Em seguida, combina as sublistas
            em ordem crescente.
           :return: Lista ordenada.
           :rtype: List<Number>.
           """
        minha_lista = deepcopy(self.__list)
        return self.__quick_sort(minha_lista)
