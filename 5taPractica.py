import networkx as nx
import matplotlib.pyplot as plt

class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])  # Path compression
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)

        if root1 != root2:
            # Union by rank
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

def kruskal(grafo, max_cost=False):
    # Inicializar el Union-Find
    union_find = UnionFind(grafo.nodes())
    arbol_expansion = nx.Graph()

    # Obtener todas las aristas y ordenarlas por peso
    aristas = [(u, v, datos['weight']) for u, v, datos in grafo.edges(data=True)]
    aristas.sort(key=lambda x: x[2], reverse=max_cost)

    # Iterar sobre las aristas ordenadas
    for u, v, peso in aristas:
        if union_find.find(u) != union_find.find(v):
            union_find.union(u, v)
            arbol_expansion.add_edge(u, v, weight=peso)
            print(f"Añadir arista: {u} -- {v} (Peso: {peso})")

    return arbol_expansion

# Crear un grafo de ejemplo para acordes musicales
grafo_acordes = nx.Graph()
grafo_acordes.add_edge('C', 'G', weight=2)
grafo_acordes.add_edge('C', 'F', weight=4)
grafo_acordes.add_edge('G', 'D', weight=3)
grafo_acordes.add_edge('F', 'Am', weight=1)
grafo_acordes.add_edge('D', 'Am', weight=5)

# Ejecutar el algoritmo de Kruskal para mínimo costo
print("Árbol de expansión de mínimo costo:")
arbol_minimo = kruskal(grafo_acordes, max_cost=False)

# Ejecutar el algoritmo de Kruskal para máximo costo
print("\nÁrbol de expansión de máximo costo:")
arbol_maximo = kruskal(grafo_acordes, max_cost=True)

# Visualizar los grafos
pos = nx.spring_layout(grafo_acordes)

plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 1)
nx.draw(grafo_acordes, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
etiquetas_peso = nx.get_edge_attributes(grafo_acordes, 'weight')
nx.draw_networkx_edge_labels(grafo_acordes, pos, edge_labels=etiquetas_peso)
plt.title("Grafo Original de Acordes")

plt.subplot(1, 3, 2)
nx.draw(arbol_minimo, pos, with_labels=True, node_color='lightgreen', node_size=2000, font_size=10, font_weight='bold')
etiquetas_peso_min = nx.get_edge_attributes(arbol_minimo, 'weight')
nx.draw_networkx_edge_labels(arbol_minimo, pos, edge_labels=etiquetas_peso_min)
plt.title("Árbol de Mínimo Costo")

plt.subplot(1, 3, 3)
nx.draw(arbol_maximo, pos, with_labels=True, node_color='salmon', node_size=2000, font_size=10, font_weight='bold')
etiquetas_peso_max = nx.get_edge_attributes(arbol_maximo, 'weight')
nx.draw_networkx_edge_labels(arbol_maximo, pos, edge_labels=etiquetas_peso_max)
plt.title("Árbol de Máximo Costo")

plt.show()
