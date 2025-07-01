import heapq

"""
Balanced Multiway Merging Sort Implementation in Python

Este programa implementa el algoritmo de ordenamiento Balanced Multiway Merging.
El algoritmo divide la lista en varias partes, las ordena y luego las fusiona de manera balanceada.
"""


def balanced_multiway_merge_sort(arr, k):
    """
    Ordena una lista usando Balanced Multiway Merging.
    :param arr: Lista de elementos a ordenar.
    :param k: Número de vías (partes) para la fusión múltiple.
    :return: Lista ordenada.
    """

    # Caso base: si la lista es pequeña, retorna ordenada
    if len(arr) <= 1:
        return arr

    # 1. Dividir la lista en k partes aproximadamente iguales
    n = len(arr)
    size = (n + k - 1) // k  # Tamaño de cada parte
    sublists = [arr[i*size : min((i+1)*size, n)] for i in range(k) if i*size < n]

    # 2. Ordenar recursivamente cada sublista
    sorted_sublists = [balanced_multiway_merge_sort(sub, k) for sub in sublists]

    # 3. Fusionar las k sublistas ordenadas usando un heap (min-heap)
    return multiway_merge(sorted_sublists)

def multiway_merge(sorted_lists):
    """
    Fusiona múltiples listas ordenadas en una sola lista ordenada.
    :param sorted_lists: Lista de listas ordenadas.
    :return: Lista fusionada y ordenada.
    """
    heap = []
    result = []

    # Inicializar el heap con el primer elemento de cada lista
    for i, sublist in enumerate(sorted_lists):
        if sublist:
            # (valor, índice de la lista, índice del elemento en la sublista)
            heapq.heappush(heap, (sublist[0], i, 0))

    # Extraer el menor elemento y agregar el siguiente de la misma sublista al heap
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        if elem_idx + 1 < len(sorted_lists[list_idx]):
            next_tuple = (sorted_lists[list_idx][elem_idx + 1], list_idx, elem_idx + 1)
            heapq.heappush(heap, next_tuple)

    return result

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de ejemplo
    arr = [34, 7, 23, 32, 5, 62, 32, 2, 12, 45, 8, 19]
    k = 3  # Número de vías para la fusión

    print("Lista original:", arr)
    sorted_arr = balanced_multiway_merge_sort(arr, k)
    print("Lista ordenada:", sorted_arr)
