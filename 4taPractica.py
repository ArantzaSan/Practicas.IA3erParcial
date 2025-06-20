import networkx as nx
import matplotlib.pyplot as plt

def prim_mst(grafo, inicio):
    # Inicialización
    arbol_parcial_minimo = nx.Graph()
    nodos_visitados = set([inicio])
    aristas = []

    # Añadir todos los nodos al árbol parcial mínimo
    for nodo in grafo.nodes():
        arbol_parcial_minimo.add_node(nodo)

    # Iterar hasta que todos los nodos estén en el árbol parcial mínimo
    while len(nodos_visitados) < grafo.number_of_nodes():
        arista_minima = None
        peso_minimo = float('inf')

        # Buscar la arista de menor peso que conecte un nodo visitado con uno no visitado
        for nodo in nodos_visitados:
            for vecino, datos in grafo[nodo].items():
                if vecino not in nodos_visitados and datos['weight'] < peso_minimo:
                    arista_minima = (nodo, vecino)
                    peso_minimo = datos['weight']

        # Añadir la arista mínima al árbol parcial mínimo
        if arista_minima:
            arbol_parcial_minimo.add_edge(*arista_minima, weight=peso_minimo)
            nodos_visitados.add(arista_minima[1])
            aristas.append((arista_minima, peso_minimo))

    return arbol_parcial_minimo, aristas

# Crear un grafo de ejemplo
grafo_servicio = nx.Graph()
grafo_servicio.add_edge('Sitio_A', 'Sitio_B', weight=4)
grafo_servicio.add_edge('Sitio_A', 'Sitio_C', weight=2)
grafo_servicio.add_edge('Sitio_B', 'Sitio_C', weight=5)
grafo_servicio.add_edge('Sitio_B', 'Sitio_D', weight=10)
grafo_servicio.add_edge('Sitio_C', 'Sitio_D', weight=3)

# Ejecutar el algoritmo de Prim
arbol_parcial_minimo, aristas = prim_mst(grafo_servicio, 'Sitio_A')

# Imprimir los resultados
print("Aristas del Árbol Parcial Mínimo:")
for arista, peso in aristas:
    print(f"Conectar {arista[0]} con {arista[1]} (Peso: {peso})")

# Visualizar el grafo original y el árbol parcial mínimo
pos = nx.spring_layout(grafo_servicio)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
nx.draw(grafo_servicio, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
etiquetas_peso = nx.get_edge_attributes(grafo_servicio, 'weight')
nx.draw_networkx_edge_labels(grafo_servicio, pos, edge_labels=etiquetas_peso)
plt.title("Grafo Original de Sitios")

plt.subplot(1, 2, 2)
nx.draw(arbol_parcial_minimo, pos, with_labels=True, node_color='lightgreen', node_size=2000, font_size=10, font_weight='bold')
etiquetas_peso_mst = nx.get_edge_attributes(arbol_parcial_minimo, 'weight')
nx.draw_networkx_edge_labels(arbol_parcial_minimo, pos, edge_labels=etiquetas_peso_mst)
plt.title("Árbol Parcial Mínimo")

plt.show()
