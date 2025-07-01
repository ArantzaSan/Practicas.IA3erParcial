"""
Ordenamiento usando Árbol Binario de Búsqueda (BST Sort)
Este programa implementa el algoritmo de ordenamiento basado en un árbol binario de búsqueda.
Los elementos se insertan en el árbol y luego se realiza un recorrido en orden (in-order traversal)
para obtener la lista ordenada.
"""

# Definición de un nodo del árbol binario de búsqueda
class NodoBST:
    def __init__(self, valor):
        self.valor = valor      # Valor almacenado en el nodo
        self.izquierda = None   # Subárbol izquierdo
        self.derecha = None     # Subárbol derecho

# Función para insertar un valor en el árbol binario de búsqueda
def insertar(nodo, valor):
    """
    Inserta un valor en el árbol binario de búsqueda.
    Si el valor es menor, va a la izquierda; si es mayor o igual, va a la derecha.
    """
    if nodo is None:
        return NodoBST(valor)
    if valor < nodo.valor:
        nodo.izquierda = insertar(nodo.izquierda, valor)
    else:
        nodo.derecha = insertar(nodo.derecha, valor)
    return nodo

# Función para recorrer el árbol en orden y recolectar los valores ordenados
def recorrido_inorden(nodo, resultado):
    """
    Realiza un recorrido inorden (izquierda, raíz, derecha) y agrega los valores a la lista resultado.
    """
    if nodo is not None:
        recorrido_inorden(nodo.izquierda, resultado)
        resultado.append(nodo.valor)
        recorrido_inorden(nodo.derecha, resultado)

# Función principal de ordenamiento usando árbol binario de búsqueda
def bst_sort(lista):
    """
    Ordena una lista utilizando un árbol binario de búsqueda.
    """
    raiz = None
    # Insertar todos los elementos en el árbol
    for valor in lista:
        raiz = insertar(raiz, valor)
    # Recorrer el árbol en orden para obtener la lista ordenada
    resultado = []
    recorrido_inorden(raiz, resultado)
    return resultado

# Ejemplo de uso
if __name__ == "__main__":
    datos = [7, 3, 9, 1, 5, 8, 2]
    print("Lista original:", datos)
    ordenada = bst_sort(datos)
    print("Lista ordenada:", ordenada)
