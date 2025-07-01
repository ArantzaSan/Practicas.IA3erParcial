# QuickSort.py
# Este programa implementa el algoritmo de ordenamiento QuickSort en Python.
# QuickSort es un algoritmo de ordenamiento eficiente basado en la técnica de divide y vencerás.

def quicksort(arr):
    """
    Función principal de QuickSort.
    Ordena una lista de elementos utilizando el algoritmo QuickSort.
    :param arr: Lista de elementos a ordenar
    :return: Lista ordenada
    """
    # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(arr) <= 1:
        return arr

    # Seleccionamos el pivote (en este caso, el último elemento)
    pivot = arr[-1]
    left = []   # Elementos menores al pivote
    right = []  # Elementos mayores o iguales al pivote

    # Recorremos todos los elementos excepto el pivote
    for x in arr[:-1]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)

    # Llamada recursiva para ordenar las sublistas y concatenamos el resultado
    return quicksort(left) + [pivot] + quicksort(right)

if __name__ == "__main__":
    # Ejemplo de uso del algoritmo QuickSort
    lista = [34, 7, 23, 32, 5, 62]
    print("Lista original:", lista)
    lista_ordenada = quicksort(lista)
    print("Lista ordenada:", lista_ordenada)
