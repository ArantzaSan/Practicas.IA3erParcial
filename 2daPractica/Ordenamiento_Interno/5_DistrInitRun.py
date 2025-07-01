# Distribution Initial Run (DIR) es un algoritmo de ordenamiento externo que distribuye los datos en varias "runs" iniciales.
# Aquí implementamos una versión simplificada para arreglos en memoria.

def distribution_initial_run(arr):
    """
    Implementa el algoritmo Distribution Initial Run para ordenar un arreglo.
    Devuelve el arreglo ordenado.
    """
    # Sección 1: Identificación de runs iniciales
    runs = []
    n = len(arr)
    i = 0
    while i < n:
        run = [arr[i]]
        i += 1
        while i < n and arr[i] >= arr[i-1]:
            run.append(arr[i])
            i += 1
        runs.append(run)

    # Sección 2: Mezcla de runs hasta obtener un solo run ordenado
    while len(runs) > 1:
        new_runs = []
        for j in range(0, len(runs), 2):
            if j+1 < len(runs):
                # Mezcla dos runs adyacentes
                merged = merge(runs[j], runs[j+1])
                new_runs.append(merged)
            else:
                # Si hay un run sin pareja, lo agregamos tal cual
                new_runs.append(runs[j])
        runs = new_runs

    # Sección 3: Retorno del resultado ordenado
    return runs[0] if runs else []

def merge(left, right):
    """
    Mezcla dos listas ordenadas en una sola lista ordenada.
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Ejemplo de uso
if __name__ == "__main__":
    arr = [5, 1, 3, 4, 2, 8, 7, 6]
    print("Arreglo original:", arr)
    sorted_arr = distribution_initial_run(arr)
    print("Arreglo ordenado:", sorted_arr)
