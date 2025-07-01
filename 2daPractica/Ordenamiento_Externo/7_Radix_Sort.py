# Radix Sort en Python
# Este programa implementa el algoritmo de ordenamiento Radix Sort para listas de números enteros.
# Radix Sort es un algoritmo de ordenamiento no comparativo que ordena los números procesando sus dígitos individuales.

def counting_sort(arr, exp):
    """
    Función auxiliar para realizar Counting Sort basado en el dígito representado por exp.
    Parámetros:
        arr: lista de enteros a ordenar parcialmente
        exp: exponente correspondiente al dígito actual (1, 10, 100, ...)
    """
    n = len(arr)
    output = [0] * n      # Lista de salida ordenada
    count = [0] * 10      # Contador para cada dígito (0-9)

    # Contar ocurrencias de cada dígito en exp
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Modificar count para que contenga la posición real de cada dígito en output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir el arreglo de salida
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copiar el arreglo ordenado a arr
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """
    Función principal para ordenar una lista usando Radix Sort.
    Parámetro:
        arr: lista de enteros a ordenar
    """
    # Encontrar el número máximo para saber el número de dígitos
    if not arr:
        return
    max_num = max(arr)

    # Aplicar counting_sort para cada dígito (exp = 1, 10, 100, ...)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de ejemplo a ordenar
    datos = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Lista original:", datos)
    radix_sort(datos)
    print("Lista ordenada:", datos)
