import heapq
def dijkstra_simulator(graph, start_node):
print(f"--- Inicio del Algoritmo de Dijkstra desde el nodo: {start_node} ---")

distances = {node: float('infinity') for node in graph}
distances[start_node] = 0

predecessors = {node: None for node in graph}

priority_queue = [(0, start_node)]
visited_nodes = set()

print("\n--- Paso 0: Inicialización ---")
print(f"Distancias iniciales: {distances}")
print(f"Cola de prioridad inicial: {priority_queue}")
print("-" * 30)

step_counter = 1

while priority_queue:
current_distance, current_node = heapq.heappop(priority_queue)

print(f"\n--- Paso {step_counter}: Explorando nodo '{current_node}' ---")
print(f"Cola de prioridad actual: {priority_queue}")
print(f"Distancia actual para '{current_node}': {current_distance}")

if current_node in visited_nodes:
print(f"Nodo '{current_node}' ya visitado con una distancia más corta. Saltando.")
continue

visited_nodes.add(current_node)
print(f"Nodos visitados hasta ahora: {visited_nodes}")

if current_distance > distances[current_node]:
print(f"Distancia extraída ({current_distance}) es mayor que la distancia actual ({distances[current_node]}) para'{current_node}'. Saltando.")
continue

print(f"Explorando vecinos de '{current_node}':")
for neighbor, weight in graph[current_node].items():
distance = current_distance + weight

print(f" Vecino: '{neighbor}', Peso de artista: {weight}")
print(f" Distancia calculada a '{neighbor}': {distance} (current distance + weight)")

if distance < distances[neighbor]:
print(f" ¡Se encontró un camino más corto a '{neighbor}'!")
print(f" Distancia anterior para '{neighbor}': {distances[neighbor]}")
print(f"    Nueva distancia para '{neighbor}': {distance}")
distances[neighbor] = distance
predecessors[neighbor] = current_node
heapq.heappush(priority_queue, (distance, neighbor))
print(f"    Se agregó '{neighbor}' a la cola de prioridad con distancia {distance}.")
else:
print(f"    No se encontró un camino más corto a '{neighbor}'.")
print(f"  Distancias actuales: {distances}")
        
print(f"Estado de las distancias después de explorar '{current_node}': {distances}")
print(f"Estado de los predecesores después de explorar '{current_node}': {predecessors}")
print("-" * 30)
step_counter += 1
  
print("\n--- Algoritmo de Dijkstra Finalizado ---")
print("\nResultados finales:")
print(f"Distancias más cortas desde '{start_node}': {distances}")
print(f"Predecesores para reconstruir caminos: {predecessors}")

def reconstruct_path(predecessors_map, target_node):
path = []
current = target_node
while current is not None:
path.insert(0, current)
current = predecessors_map[current]
return path if path[0] == start_node else [] # Asegura que el camino empiece en el origen

print("\nCaminos más cortos:")
for node in graph:
if node != start_node:
path = reconstruct_path(predecessors, node)
print(f"  Camino de '{start_node}' a '{node}': {' -> '.join(path)} (Distancia: {distances[node]})")

if __name__ == "__main__":
    # Definición del grafo (puedes modificarlo)
graph1 = {
'A': {'B': 1, 'C': 4},
'B': {'A': 1, 'D': 2, 'E': 5},
'C': {'A': 4, 'F': 2},
'D': {'B': 2, 'G': 1},
'E': {'B': 5, 'F': 3},
'F': {'C': 2, 'E': 3, 'G': 1},
'G': {'D': 1, 'F': 1}
}

graph2 = {
 '1': {'2': 7, '3': 9, '6': 14},
 '2': {'1': 7, '3': 10, '4': 15},
 '3': {'1': 9, '2': 10, '4': 11, '6': 2},
 '4': {'2': 15, '3': 11, '5': 6},
 '5': {'4': 6, '6': 9},
 '6': {'1': 14, '3': 2, '5': 9}
 }

 print("--- Simulador de Dijkstra con Grafo 1 ---")
 dijkstra_simulator(graph1, 'A')

 print("\n" + "=" * 50 + "\n")

 print("--- Simulador de Dijkstra con Grafo 2 ---")
 dijkstra_simulator(graph2, '1')


