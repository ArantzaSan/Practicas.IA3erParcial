# Algoritmo de ordenamiento por inserción (Insertion Sort) en Python

def insertion_sort(arr):
    """
    Ordena una lista utilizando el algoritmo de inserción.
    :param arr: Lista de elementos a ordenar
    :return: None (la lista se ordena en el lugar)
    """
    # Recorremos la lista desde el segundo elemento hasta el final
    for i in range(1, len(arr)):
        key = arr[i]  # Elemento actual a insertar en la parte ordenada
        j = i - 1
        # Desplazamos los elementos mayores que key una posición adelante
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Insertamos el elemento en la posición correcta
        arr[j + 1] = key

# Ejemplo de uso del algoritmo
if __name__ == "__main__":
    # Definimos una lista desordenada
    lista = [5, 2, 9, 1, 5, 6]
    print("Lista original:", lista)
    # Llamamos a la función de ordenamiento
    insertion_sort(lista)
    # Mostramos la lista ordenada
    print("Lista ordenada:", lista)
