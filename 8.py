import heapq
import numpy as np


def find_paths(graph, start, end, path=[]):
    # Esta línea agrega el nodo de inicio al camino actual
    path = path + [start]
    if start == end:  # Si el nodo de inicio es igual al nodo final a encontrado un camino, devuelve ese camino
        return [path]
    if start not in graph:  # Si el nodo de inicio no está en el grafo no hay ningún camino posible, devuelve una lista vacía
        return []
    paths = []  # Inicializa paths
    for node in graph[start]:  # recorre todos los nodos conectados al nodo de inicio
        # verifica si el nodo actual ya está en el camino (evitar ciclos)
        if node not in path:
            # recursiva para continuar buscando caminos desde el nodo actual hasta el nodo final
            newpaths = find_paths(graph, node, end, path)
            for newpath in newpaths:  # Agregar todos los nuevos caminos encontrados a la lista de caminos
                paths.append(newpath)
    return paths


# Definimos el grafo
graph = {'A': ['B', 'C', 'D', 'E', 'F', 'G', 'H'],
         'B': ['A', 'C', 'D', 'E', 'F', 'G', 'H'],
         'C': ['A', 'B', 'D', 'E', 'F', 'G', 'H'],
         'D': ['A', 'B', 'C', 'E', 'F', 'G', 'H'],
         'E': ['A', 'B', 'C', 'D', 'F', 'G', 'H'],
         'F': ['A', 'B', 'C', 'D', 'E', 'G', 'H'],
         'G': ['A', 'B', 'C', 'D', 'E', 'F', 'H'],
         'H': ['A', 'B', 'C', 'D', 'E', 'F', 'G']}

# Buscamos todos los caminos de A a B
paths = find_paths(graph, 'A', 'B')
for path in paths:
    print(path)


def dijkstra(graph, start):
    n = len(graph)
    dist = [np.inf]*n
    prev = [None]*n
    dist[start] = 0
    queue = [(0, start)]

    while queue:
        path_len, v = heapq.heappop(queue)
        if path_len == dist[v]:
            for w, edge_len in enumerate(graph[v]):
                if edge_len > 0 and path_len + edge_len < dist[w]:
                    dist[w] = path_len + edge_len
                    heapq.heappush(queue, (dist[w], w))
                    prev[w] = v
    return dist, prev


# Generamos una matriz de adyacencia con valores aleatorios
np.random.seed(0)  # Para reproducibilidad
graph = np.random.randint(1, 10, size=(8, 8))

# Aseguramos que la diagonal sea 0 (no hay bucles)
np.fill_diagonal(graph, 0)

# Aseguramos que la matriz sea simétrica (grafo no dirigido)
graph = np.maximum(graph, graph.T)

# Imprimimos la matriz de adyacencia
print("Matriz de adyacencia:")
print(graph)

# Calculamos el camino más corto de A (0) a B (1)
dist, prev = dijkstra(graph, 0)
print("\nDistancia más corta de A a B:", dist[1])
