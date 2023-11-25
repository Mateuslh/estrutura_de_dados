from vertice import Vertice

nove = Vertice("Nove")
oito = Vertice("Oito")
dois = Vertice("Dois")
dez = Vertice("Dez")

nove.adicionar_adjacente(oito, 20)
nove.adicionar_adjacente(dois, 15)
nove.adicionar_adjacente(dez, 10)

oito.adicionar_adjacente(dois, 20)
oito.adicionar_adjacente(nove, 20)

dois.adicionar_adjacente(oito, 20)
dois.adicionar_adjacente(nove, 15)
dois.adicionar_adjacente(dez, 5)

dez.adicionar_adjacente(dois, 5)
dez.adicionar_adjacente(nove, 10)

print("\nNove")
nove.mostra_adjacentes()
print(nove.retornar_adjacente(oito))

print("\nOito")
oito.mostra_adjacentes()
print(oito.retornar_adjacente(nove))

print("\nDois")
dois.mostra_adjacentes()
print(dois.retornar_adjacente(dez))

print("\nDez")
dez.mostra_adjacentes()
print(dez.retornar_adjacente(dois))