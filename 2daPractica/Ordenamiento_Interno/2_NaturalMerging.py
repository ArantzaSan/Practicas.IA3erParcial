# Natural Merging Sort en Python
# Este algoritmo detecta secuencias ordenadas (runs) en la lista y las fusiona hasta que toda la lista está ordenada.

def encontrar_runs(arr):
    """
    Encuentra las secuencias ordenadas (runs) en la lista.
    Devuelve una lista de tuplas (inicio, fin) para cada run.
    """
    runs = []
    n = len(arr)
    i = 0
    while i < n:
        start = i
        # Avanza mientras la secuencia esté ordenada
        while i + 1 < n and arr[i] <= arr[i + 1]:
            i += 1
        runs.append((start, i))
        i += 1
    return runs

def fusionar(arr, inicio1, fin1, inicio2, fin2):
    """
    Fusiona dos runs consecutivos [inicio1, fin1] y [inicio2, fin2] en la lista arr.
    """
    temp = []
    i, j = inicio1, inicio2
    while i <= fin1 and j <= fin2:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    # Añadir elementos restantes de ambos runs
    temp.extend(arr[i:fin1+1])
    temp.extend(arr[j:fin2+1])
    # Copiar la fusión de vuelta al arreglo original
    arr[inicio1:fin2+1] = temp

def natural_merging_sort(arr):
    """
    Implementa el algoritmo de Natural Merging Sort.
    """
    n = len(arr)
    if n <= 1:
        return arr

    while True:
        runs = encontrar_runs(arr)
        # Si solo hay un run, la lista ya está ordenada
        if len(runs) == 1:
            break
        # Fusionar pares de runs consecutivos
        i = 0
        while i < len(runs) - 1:
            inicio1, fin1 = runs[i]
            inicio2, fin2 = runs[i+1]
            fusionar(arr, inicio1, fin1, inicio2, fin2)
            i += 2
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    lista = [5, 1, 4, 2, 8, 3, 7, 6]
    print("Lista original:", lista)
    natural_merging_sort(lista)
    print("Lista ordenada:", lista)
