# polyphase_sort.py
# Implementación del algoritmo de ordenamiento Polyphase Sort en Python
# Este algoritmo es útil para ordenar archivos grandes que no caben en memoria,
# utilizando archivos temporales y el método de mezcla externa.

import os
import heapq

def split_into_runs(input_file, run_size):
    """
    Divide el archivo de entrada en runs (subsecuencias ordenadas) de tamaño run_size.
    Cada run se escribe en un archivo temporal.
    Retorna la lista de archivos temporales generados.
    """
    runs = []
    with open(input_file, 'r') as f:
        while True:
            lines = []
            for _ in range(run_size):
                line = f.readline()
                if not line:
                    break
                lines.append(int(line.strip()))
            if not lines:
                break
            lines.sort()
            run_file = f'run_{len(runs)}.tmp'
            with open(run_file, 'w') as rf:
                for item in lines:
                    rf.write(f"{item}\n")
            runs.append(run_file)
    return runs

def merge_runs(run_files, output_file):
    """
    Realiza la mezcla de los runs usando un heap (mezcla k-vías).
    El resultado se escribe en output_file.
    """
    files = [open(run, 'r') for run in run_files]
    heap = []
    for idx, f in enumerate(files):
        line = f.readline()
        if line:
            heapq.heappush(heap, (int(line.strip()), idx))
    with open(output_file, 'w') as out:
        while heap:
            value, idx = heapq.heappop(heap)
            out.write(f"{value}\n")
            line = files[idx].readline()
            if line:
                heapq.heappush(heap, (int(line.strip()), idx))
    for f in files:
        f.close()

def polyphase_sort(input_file, output_file, run_size=100):
    """
    Función principal que ejecuta el Polyphase Sort.
    1. Divide el archivo en runs ordenados.
    2. Mezcla los runs hasta obtener el archivo ordenado final.
    """
    # Paso 1: Crear runs ordenados
    runs = split_into_runs(input_file, run_size)
    
    # Paso 2: Mezclar los runs (en Polyphase real, se usan patrones de Fibonacci para optimizar,
    # aquí hacemos una mezcla k-vías simple para ilustrar el proceso)
    if len(runs) == 1:
        os.rename(runs[0], output_file)
    else:
        merge_runs(runs, output_file)
        # Limpiar archivos temporales
        for run in runs:
            os.remove(run)

if __name__ == "__main__":
    # Ejemplo de uso:
    # Crear un archivo de entrada con números desordenados, uno por línea.
    input_file = "input.txt"
    output_file = "sorted.txt"
    run_size = 100  # Ajustar según la memoria disponible

    polyphase_sort(input_file, output_file, run_size)
    print(f"Archivo ordenado generado: {output_file}")

"""
Notas:
- Este código es una simplificación del Polyphase Sort real, que utiliza patrones de distribución de runs
  basados en la secuencia de Fibonacci para minimizar el número de archivos temporales y lecturas/escrituras.
- Para un Polyphase Sort completo, se requiere una lógica más compleja para distribuir y mezclar los runs
  entre varios archivos temporales siguiendo la secuencia de Fibonacci.
- Este ejemplo ilustra el flujo general: partición en runs y mezcla externa.
"""
