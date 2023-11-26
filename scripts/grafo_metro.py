import sys

domain = sys.path[0].replace("scripts", "domain")
sys.path.append(domain)

import grafo as g

grafoMetro = g.Grafo("Metro São Paulo")

vila_natal = grafoMetro.adiciona_vertice("Vila Natal")
capao_redondo = grafoMetro.adiciona_vertice("Capão Redondo")
santo_amaro = grafoMetro.adiciona_vertice("Santo Amaro")
pinheiros = grafoMetro.adiciona_vertice("Pinheiros")
vila_sonia = grafoMetro.adiciona_vertice("Vila Sônia")
osasco = grafoMetro.adiciona_vertice("Osasco")
itapevi = grafoMetro.adiciona_vertice("Itapevi")
paulista = grafoMetro.adiciona_vertice("Paulista")
vila_madalena = grafoMetro.adiciona_vertice("Vila Madalena")
paraiso = grafoMetro.adiciona_vertice("Paraíso")
republica = grafoMetro.adiciona_vertice("República")
barra_funda = grafoMetro.adiciona_vertice("Barra Funda")
praca_se = grafoMetro.adiciona_vertice("Sé")
luz = grafoMetro.adiciona_vertice("Luz")
tucuruvi = grafoMetro.adiciona_vertice("Tucuruvi")
jundiai = grafoMetro.adiciona_vertice("Jundiaí")
jabaquara = grafoMetro.adiciona_vertice("Jabaquara")
tamanduatei = grafoMetro.adiciona_vertice("Tamanduateí")
bras = grafoMetro.adiciona_vertice("Brás")
rio_grande_da_serra = grafoMetro.adiciona_vertice("Rio Grande da Serra")
jardim_colonial = grafoMetro.adiciona_vertice("Jardim Colonial")
artur_alvim = grafoMetro.adiciona_vertice("Artur Alvim")
estudantes = grafoMetro.adiciona_vertice("Estudantes")
aracare = grafoMetro.adiciona_vertice("Aracaré")
eng_goulart = grafoMetro.adiciona_vertice("Engº Goulart")
guarulhos = grafoMetro.adiciona_vertice("Guarulhos")

vila_natal.adicionar_adjacente(santo_amaro, 6)

capao_redondo.adicionar_adjacente(santo_amaro, 4)

santo_amaro.adicionar_adjacente(vila_natal, 6)
santo_amaro.adicionar_adjacente(capao_redondo, 4)
santo_amaro.adicionar_adjacente(pinheiros, 8)
santo_amaro.adicionar_adjacente(paraiso, 14)

pinheiros.adicionar_adjacente(santo_amaro, 8)
pinheiros.adicionar_adjacente(vila_sonia, 3)
pinheiros.adicionar_adjacente(osasco, 5)
pinheiros.adicionar_adjacente(paulista, 4)

paraiso.adicionar_adjacente(santo_amaro, 14)
paraiso.adicionar_adjacente(paulista, 3)
paraiso.adicionar_adjacente(praca_se, 4)
paraiso.adicionar_adjacente(jabaquara, 8)
paraiso.adicionar_adjacente(tamanduatei, 6)

vila_sonia.adicionar_adjacente(pinheiros, 3)

osasco.adicionar_adjacente(pinheiros, 5)
osasco.adicionar_adjacente(itapevi, 13)
osasco.adicionar_adjacente(barra_funda, 5)

paulista.adicionar_adjacente(pinheiros, 4)
paulista.adicionar_adjacente(vila_madalena, 3)
paulista.adicionar_adjacente(republica, 2)
paulista.adicionar_adjacente(paraiso, 3)

itapevi.adicionar_adjacente(osasco, 13)

barra_funda.adicionar_adjacente(osasco, 5)
barra_funda.adicionar_adjacente(jundiai, 16)
barra_funda.adicionar_adjacente(republica, 3)

jundiai.adicionar_adjacente(barra_funda, 16)

vila_madalena.adicionar_adjacente(paulista, 3)

republica.adicionar_adjacente(paulista, 2)
republica.adicionar_adjacente(praca_se, 2)
republica.adicionar_adjacente(barra_funda, 3)
republica.adicionar_adjacente(luz, 1)

praca_se.adicionar_adjacente(republica, 2)
praca_se.adicionar_adjacente(paraiso, 4)
praca_se.adicionar_adjacente(luz, 2)
praca_se.adicionar_adjacente(bras, 2)

luz.adicionar_adjacente(republica, 1)
luz.adicionar_adjacente(praca_se, 2)
luz.adicionar_adjacente(bras, 1)
luz.adicionar_adjacente(tucuruvi, 8)

jabaquara.adicionar_adjacente(paraiso, 8)

tamanduatei.adicionar_adjacente(paraiso, 6)
tamanduatei.adicionar_adjacente(rio_grande_da_serra, 9)
tamanduatei.adicionar_adjacente(jardim_colonial, 11)
tamanduatei.adicionar_adjacente(bras, 3)

rio_grande_da_serra.adicionar_adjacente(tamanduatei, 9)

jardim_colonial.adicionar_adjacente(tamanduatei, 11)

bras.adicionar_adjacente(tamanduatei, 3)
bras.adicionar_adjacente(artur_alvim, 9)
bras.adicionar_adjacente(estudantes, 14)
bras.adicionar_adjacente(eng_goulart, 2)
bras.adicionar_adjacente(praca_se, 2)
bras.adicionar_adjacente(luz, 1)

artur_alvim.adicionar_adjacente(bras, 9)

estudantes.adicionar_adjacente(bras, 14)

eng_goulart.adicionar_adjacente(bras, 2)
eng_goulart.adicionar_adjacente(aracare, 10)
eng_goulart.adicionar_adjacente(guarulhos, 2)

aracare.adicionar_adjacente(eng_goulart, 10)

guarulhos.adicionar_adjacente(eng_goulart, 2)

tucuruvi.adicionar_adjacente(luz, 8)

grafoMetro.mostra_vertices()