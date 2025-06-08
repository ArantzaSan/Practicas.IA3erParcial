import heapq
class UnionFind:

  def __init__(self, nodes):
    self.parent = {node: node for node in nodes}
    self.rank = {node: 0 for node in nodes}
    print(f"  [Union-Find] Inicializado. Cada nodo en su propio conjunto: {self.parent}")

def find(self, i):
  if self.parent[i] == i:
    return i
  self.parent[i] = self.find(self.parent[i])
  return self.parent[i]

def union(self, i, j):
  root_i = self.find(i)
  root_j = self.find(j)

if root_i != root_j:
  if self.rank[root_i] < self.rank[root_j]
self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            print(f"  [Union-Find] Se unieron los conjuntos de '{i}' y '{j}'. Nuevos padres: {self.parent}")
            return True
        else:
            print(f"  [Union-Find] '{i}' y '{j}' ya están en el mismo conjunto. Esta arista formaría un ciclo.")
            return False

def kruskal_simulator(graph_edges, num_nodes, mode="min"):
  
if not graph_edges:
        print("El grafo no tiene aristas.")
        return [], 0

    mst_edges = []
    total_cost = 0
   if mode == "min":
        sorted_edges = sorted(graph_edges, key=lambda item: item[2])
        print(f"--- Iniciando simulador de Kruskal (Árbol de MÍNIMO Costo) ---")
        print(f"Aristas ordenadas por peso (de menor a mayor): {sorted_edges}")
    elif mode == "max":

processed_edges = [ (u, v, -w) for u, v, w in graph_edges]
        sorted_edges = sorted(processed_edges, key=lambda item: item[2])
        print(f"--- Iniciando simulador de Kruskal (Árbol de MÁXIMO Costo) ---")
        print(f"Aristas ordenadas por 'peso negativo' (para simular el mayor peso original): {sorted_edges}")
    else:
        print("Modo inválido. Use 'min' o 'max'.")
        return [], 0

uf = UnionFind(num_nodes)
step = 0
for u, v, weight_processed in sorted_edges:
        step += 1
original_weight = -weight_processed if mode == "max" else weight_processed

        print(f"\n--- Paso {step} ---")
        print(f"Considerando la arista: ({u} - {v}, peso original: {original_weight})")
if uf.union(u, v): # uf.union devuelve True si no formó un ciclo y se unió
            mst_edges.append((u, v, original_weight))
            total_cost += original_weight
            print(f"  ¡Añadimos la arista ({u} - {v}, peso: {original_weight}) al Árbol Parcial!")
            print(f"  Aristas actuales en el Árbol Parcial: {mst_edges}")
            print(f"  Costo total actual: {total_cost}")
else:
            print(f"  Esta arista se descartó porque formaría un ciclo en el Árbol Parcial.")
        
    if len(mst_edges) == len(num_nodes) - 1:
            print(f"\n¡Se han conectado todos los nodos ({len(num_nodes)-1} aristas)! Terminando antes de tiempo.")
            break

    if len(mst_edges) < len(num_nodes) - 1:
        print("\n¡Advertencia! No se pudo conectar todos los nodos. El grafo puede no ser conexo.")
        print(f"Nodos conectados: {set([n for edge in mst_edges for n in [edge[0], edge[1]]])}")

    print(f"\n--- ¡Simulación de Kruskal completada ({'MÍNIMO' if mode=='min' else 'MÁXIMO'} Costo)! ---")
    print("\nÁrbol Parcial Resultante:")
    for u, v, weight in mst_edges:
        print(f"  {u} --({weight})-- {v}")
    print(f"Costo total del Árbol Parcial: {total_cost}")

    return mst_edges, total_cost

if __name__ == "__main__":
    # Definición de un grafo como lista de aristas (origen, destino, peso)
    # Nodos: A, B, C, D, E, F, G
    edges1 = [
        ('A', 'B', 7), ('A', 'D', 5),
        ('B', 'C', 8), ('B', 'D', 9), ('B', 'E', 7),
        ('C', 'E', 5),
        ('D', 'E', 15), ('D', 'F', 6),
        ('E', 'F', 8), ('E', 'G', 9),
        ('F', 'G', 11)
    ]
    nodes1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    print("--- Simulando para el Grafo 1 (MÍNIMO Costo) ---")
    kruskal_simulator(edges1, nodes1, mode="min")

    print("\n" + "="*80 + "\n") # Separador

    print("--- Simulando para el Grafo 1 (MÁXIMO Costo) ---")
    kruskal_simulator(edges1, nodes1, mode="max")

    print("\n" + "="*80 + "\n") # Separador

    # Otro ejemplo de grafo
    edges2 = [
        ('0', '1', 4), ('0', '7', 8),
        ('1', '2', 8), ('1', '7', 11),
        ('2', '3', 7), ('2', '5', 4), ('2', '8', 2),
        ('3', '4', 9), ('3', '5', 14),
        ('4', '5', 10),
        ('5', '6', 2),
        ('6', '7', 1), ('6', '8', 6),
        ('7', '8', 7)
    ]
    nodes2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

    print("--- Simulando para el Grafo 2 (MÍNIMO Costo) ---")
    kruskal_simulator(edges2, nodes2, mode="min")

    print("\n" + "="*80 + "\n") # Separador

    # Grafo desconectado para mostrar la advertencia
    edges_disconnected = [
        ('X', 'Y', 10),
        ('P', 'Q', 20)
    ]
    nodes_disconnected = ['X', 'Y', 'P', 'Q']

    print("--- Simulando para un Grafo Desconectado (MÍNIMO Costo) ---")
    kruskal_simulator(edges_disconnected, nodes_disconnected, mode="min")

