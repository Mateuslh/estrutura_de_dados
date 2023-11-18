import os
import unittest
import random
import string
from os import environ
from dotenv import load_dotenv

from domain.Ordenador import Ordenador

load_dotenv()
class TestOrdenador(unittest.TestCase):

    def setUp(self):
        tamanho_lista_teste = int(os.environ["Ordenador_tamanho_lista_teste"])
        lista_numeros = [random.randint(1, 100) for _ in range(tamanho_lista_teste)]
        lista_numero_string =  [''.join(random.choices(string.ascii_letters + string.digits, k=8)) for _ in range(tamanho_lista_teste)]
        self.registros_validos = lista_numeros
        self.registros_invalidos = lista_numero_string
        lista_numeros.sort(reverse=True)
        self.registros_invertidos = lista_numeros
        lista_numeros.sort()
        self.resultado_ordenado = lista_numeros

    def test_bubble_sort(self):
        ordenador = Ordenador(self.registros_validos)
        resultado = ordenador.bubble_sort()
        self.assertEqual(resultado.retorno, self.resultado_ordenado)

    def test_insertion_sort(self):
        ordenador = Ordenador(self.registros_validos)
        resultado = ordenador.insertion_sort()
        self.assertEqual(resultado.retorno, self.resultado_ordenado)

    def test_merge_sort(self):
        ordenador = Ordenador(self.registros_validos)
        resultado = ordenador.merge_sort()
        self.assertEqual(resultado.retorno, self.resultado_ordenado)

    def test_quick_sort(self):
        ordenador = Ordenador(self.registros_validos)
        resultado = ordenador.quick_sort()
        self.assertEqual(resultado.retorno, self.resultado_ordenado)

    def test_registros_invalidos(self):
        with self.assertRaises(ValueError):
            ordenador = Ordenador(self.registros_invalidos)

    def test_bubble_sort_lista_vazia(self):
        ordenador = Ordenador([])
        resultado = ordenador.bubble_sort()
        self.assertEqual(resultado.retorno, [])

    def test_insertion_sort_lista_vazia(self):
        ordenador = Ordenador([])
        resultado = ordenador.insertion_sort()
        self.assertEqual(resultado.retorno, [])

    def test_merge_sort_lista_vazia(self):
        ordenador = Ordenador([])
        resultado = ordenador.merge_sort()
        self.assertEqual(resultado.retorno, None)

    def test_quick_sort_lista_vazia(self):
        ordenador = Ordenador([])
        resultado = ordenador.quick_sort()
        self.assertEqual(resultado.retorno, [])

    def test_quick_sort_lista_ordenada_descendente(self):
        ordenador = Ordenador(self.registros_invertidos)
        resultado = ordenador.quick_sort()
        self.assertEqual(resultado.retorno, self.registros_validos)

    def test_bubble_sort_lista_ordenada_descendente(self):
        ordenador = Ordenador(self.registros_invertidos)
        resultado = ordenador.bubble_sort()
        self.assertEqual(resultado.retorno, self.registros_validos)

    def test_insertion_sort_lista_ordenada_descendente(self):
        ordenador = Ordenador(self.registros_invertidos)
        resultado = ordenador.insertion_sort()
        self.assertEqual(resultado.retorno, self.registros_validos)

    def test_merge_sort_lista_ordenada_descendente(self):
        ordenador = Ordenador(self.registros_invertidos)
        resultado = ordenador.merge_sort()
        self.assertEqual(resultado.retorno, self.registros_validos)

if __name__ == '__main__':
    unittest.main()
