# 2.Seleccion.py
# Algoritmo de ordenamiento por selección (Selection Sort)
# Este programa implementa el algoritmo de selección para ordenar una lista de números.
# Cada sección del código está comentada para explicar su funcionamiento.

def selectionSort(arr):
    """
    Ordena una lista utilizando el algoritmo de selección.
    :param arr: Lista de elementos a ordenar
    :return: None (la lista se ordena en el lugar)
    """
    n = len(arr)
    # Recorremos toda la lista
    for i in range(n):
        # Suponemos que el elemento actual es el mínimo
        min_idx = i
        # Buscamos el elemento más pequeño en el resto de la lista
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiamos el elemento más pequeño encontrado con el primer elemento no ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Función principal para probar el algoritmo
if __name__ == "__main__":
    # Lista de ejemplo a ordenar
    lista = [64, 25, 12, 22, 11]
    print("Lista original:", lista)
    # Llamamos a la función de ordenamiento
    selectionSort(lista)
    # Mostramos la lista ordenada
    print("Lista ordenada:", lista)
