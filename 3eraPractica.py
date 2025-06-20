import networkx as nx
import matplotlib.pyplot as plt
import heapq

def dijkstra(grafo, inicio):
    # Inicialización
    distancias = {nodo: float('infinity') for nodo in grafo}
    distancias[inicio] = 0
    cola_prioridad = [(0, inicio)]
    camino = {nodo: [] for nodo in grafo}

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if distancia_actual > distancias[nodo_actual]:
            continue

        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso

            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola_prioridad, (distancia, vecino))
                camino[vecino] = camino[nodo_actual] + [nodo_actual]

    return distancias, camino

# Crear un grafo de ejemplo
grafo_musical = {
    'Pieza_A': {'Pieza_B': 4, 'Pieza_C': 2},
    'Pieza_B': {'Pieza_A': 4, 'Pieza_C': 5, 'Pieza_D': 10},
    'Pieza_C': {'Pieza_A': 2, 'Pieza_B': 5, 'Pieza_D': 3},
    'Pieza_D': {'Pieza_B': 10, 'Pieza_C': 3}
}

# Ejecutar el algoritmo de Dijkstra
distancias, camino = dijkstra(grafo_musical, 'Pieza_A')

# Imprimir los resultados
print("Distancias más cortas desde Pieza_A:")
for nodo, distancia in distancias.items():
    print(f"{nodo}: {distancia}")

print("\nCaminos más cortos desde Pieza_A:")
for nodo, path in camino.items():
    print(f"{nodo}: {' -> '.join([ 'Pieza_A'] + path) if path else 'Pieza_A'}")

# Visualizar el grafo
G = nx.Graph()

for nodo, vecinos in grafo_musical.items():
    for vecino, peso in vecinos.items():
        G.add_edge(nodo, vecino, weight=peso)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
etiquetas_peso = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas_peso)
plt.title("Grafo de Piezas Musicales")
plt.show()
