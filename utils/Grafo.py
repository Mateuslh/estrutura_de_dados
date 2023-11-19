import heapq

def dijkstra(grafo, origem, destino):
    if not grafo.vertice_existe(origem) or not grafo.vertice_existe(destino):
        raise ValueError("Vértice de origem ou destino não existe no grafo.")

    distancia = {v: float('infinity') for v in grafo.vertices}
    distancia[origem] = 0
    heap = [(0, origem)]

    while heap:
        dist_atual, vertice_atual = heapq.heappop(heap)

        if dist_atual > distancia[vertice_atual]:
            continue

        for vizinho in grafo.busca_vertices_adjacentes(vertice_atual):
            peso = grafo.peso_aresta(vertice_atual, vizinho)
            nova_distancia = distancia[vertice_atual] + peso

            if nova_distancia < distancia[vizinho]:
                distancia[vizinho] = nova_distancia
                heapq.heappush(heap, (nova_distancia, vizinho))
    caminho = [destino]
    vertice_atual = destino
    while vertice_atual != origem:
        for vizinho in grafo.busca_vertices_adjacentes(vertice_atual):
            if distancia[vizinho] + grafo.peso_aresta(vizinho, vertice_atual) == distancia[vertice_atual]:
                caminho.append(vizinho)
                vertice_atual = vizinho
                break

    return list(reversed(caminho)), distancia[destino]