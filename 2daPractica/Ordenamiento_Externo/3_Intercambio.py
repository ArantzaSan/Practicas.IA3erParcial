# Algoritmo de Ordenamiento por Intercambio (Bubble Sort)
# Este programa ordena una lista de números utilizando el método de intercambio.

def intercambio(lista):
    """
    Ordena una lista utilizando el algoritmo de intercambio (bubble sort).
    :param lista: Lista de elementos a ordenar
    :return: Lista ordenada
    """
    n = len(lista)
    # Recorremos toda la lista
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n - i - 1):
            # Intercambiamos si el elemento encontrado es mayor que el siguiente
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def main():
    # Lista de ejemplo a ordenar
    datos = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", datos)
    
    # Ordenamos la lista usando el algoritmo de intercambio
    lista_ordenada = intercambio(datos.copy())
    print("Lista ordenada:", lista_ordenada)

if __name__ == "__main__":
    main()
