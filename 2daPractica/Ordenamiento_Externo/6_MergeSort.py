# Implementación del algoritmo MergeSort en Python

def merge_sort(arr):
    """
    Función para realizar merge sort en una lista.
    """
    if len(arr) > 1:
        # Encontrar el punto medio y dividir el arreglo
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Ordenar recursivamente ambas mitades
        merge_sort(left_half)
        merge_sort(right_half)

        # Mezclar las mitades ordenadas
        i = j = k = 0

        # Copiar datos a los arreglos temporales left_half[] y right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Verificar si quedó algún elemento en left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Verificar si quedó algún elemento en right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Sección principal para probar la función merge_sort
if __name__ == "__main__":
    # Lista de ejemplo para ordenar
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Arreglo original:", arr)
    merge_sort(arr)
    print("Arreglo ordenado:", arr)
