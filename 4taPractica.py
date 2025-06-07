import heapq

def prim_mst_simulator(graph):

if not graph:
  print("El grafo está vacío")
  return [], 0

mst_nodes = set()
mst_edges = []
total_cost = 0

priority_queue = []
start_node = list(graph.keys())[0]

print(f"\nPaso 1: Añadiendo el nodo inicial '{start_node}' al MST.")
print(f"Nodos en MST: {mst_nodes}")

for neighbor, weight in graph[start_node]:
  heapq.heappush(priority_queue, (weight, start_node, neighbor))
print(f"Aristas candidatas en la cola de prioridad (peso, origen, destino): {priority_queue}")

step = 1
while priority_queue and len(mst_nodes) < len(graph):
  step += 1
  print(f"\n--- Paso {step} ---")

  weight, u, v = heapq.heappop(priority_queue)
  print(f"Extraemos la arista con menor peso de la cola: ({u} - {v}, peso: {weight})")

if v in mst_nodes:
  print(f"El nodo '{v}' ya está en el MST. Esta arista crearía un ciclo, la ignoramos.")
  print(f"Nodos en MST: {mst_nodes}")
  print(f"Aristas en MST: {mst_edges}")
  print(f"Costo total actual: {total_cost}")
  print(f"Aristas candidatas en la cola de prioridad: {priority_queue}")
    continue
mst_nodes.add(v)
        mst_edges.append((u, v, weight))
        total_cost += weight

        print(f"Añadimos el nodo '{v}' al MST.")
        print(f"Añadimos la arista ({u} - {v}, peso: {weight}) al MST.")
        print(f"Nodos en MST: {mst_nodes}")
        print(f"Aristas en MST: {mst_edges}")
        print(f"Costo total actual: {total_cost}")
print(f"Explorando vecinos de '{v}':")
        for neighbor, edge_weight in graph[v]:
            if neighbor not in mst_nodes:
                heapq.heappush(priority_queue, (edge_weight, v, neighbor))
                print(f"  Añadiendo arista candidata ({v} - {neighbor}, peso: {edge_weight}) a la cola.")
        print(f"Aristas candidatas en la cola de prioridad: {priority_queue}")

if len(mst_nodes) != len(graph):
        print("\n¡Advertencia! No se pudo conectar todos los nodos. El grafo puede no ser conexo.")
        return mst_edges, total_cost

    print("\n--- ¡Simulación de Prim completada! ---")
    print("\nÁrbol Parcial Mínimo (MST):")
    for u, v, weight in mst_edges:
        print(f"  {u} --({weight})-- {v}")
    print(f"Costo total del MST: {total_cost}")

    return mst_edges, total_cost

 --- Ejemplo de uso ---
if __name__ == "__main__":
    # Definición de un grafo (ejemplo de Wikipedia para Prim)
    # Nodos: A, B, C, D, E, F, G
    # Aristas y sus pesos
    graph1 = {
        'A': [('B', 7), ('D', 5)],
        'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
        'C': [('B', 8), ('E', 5)],
        'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
        'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],
        'F': [('D', 6), ('E', 8), ('G', 11)],
        'G': [('E', 9), ('F', 11)]
    }

    print("Simulando para el Grafo 1:")
    prim_mst_simulator(graph1)

    print("\n" + "="*50 + "\n")

    # Otro ejemplo de grafo
    graph2 = {
        '0': [('1', 4), ('7', 8)],
        '1': [('0', 4), ('2', 8), ('7', 11)],
        '2': [('1', 8), ('3', 7), ('5', 4), ('8', 2)],
        '3': [('2', 7), ('4', 9), ('5', 14)],
        '4': [('3', 9), ('5', 10)],
        '5': [('2', 4), ('3', 14), ('4', 10), ('6', 2)],
        '6': [('5', 2), ('7', 1), ('8', 6)],
        '7': [('0', 8), ('1', 11), ('6', 1), ('8', 7)],
        '8': [('2', 2), ('6', 6), ('7', 7)]
    }

    print("Simulando para el Grafo 2:")
    prim_mst_simulator(graph2)

    print("\n" + "="*50 + "\n")

    # Grafo desconectado para mostrar la advertencia
    graph_disconnected = {
        'A': [('B', 1)],
        'B': [('A', 1)],
        'C': [('D', 2)],
        'D': [('C', 2)]
    }
    print("Simulando para un Grafo Desconectado:")
    prim_mst_simulator(graph_disconnected)
