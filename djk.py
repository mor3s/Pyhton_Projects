from heapq import  heappop, heappush


#Def
# Etant donné un graph orienté et des poids positifs ou nul sur les arcs, on cherche un plus court
#chemin entre une source et une destination

#Complexité
#En implementation brutale, on est en O(|V|²), et si on utilise une file de priorité on peut
#faire tomber la complexité a O(|E|log|V|)

#

def dijkstra(graph, weight, source=0, target=None):
    """single source shortest paths by Dijkstra
           :param graph: directed graph in listlist or listdict format
           :param weight: in matrix format or same listdict graph
           :assumes: weights are non-negative
           :param source: source vertex
           :type source: int
           :param target: if given, stops once distance to target found
           :type target: int
           :returns: distance table, precedence table
           :complexity: `O(|V| + |E|log|V|)`
    """
    n = len(graph)
    assert all (weight[u][v] >= 0 for u in range(n) for v in graph[u])
    prec = [None] * n
    black = [False] * n
    dist = [float('inf')] * n
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        dist_node, node = heappop(heap)   # le sommet le plus proche
        if not black[node]:
            black[node] = True
            if node == target:
                break
            for neighbor in graph[node]:
                dist_neighbor = dist_node + weight[node][neighbor]
                if dist_neighbor < dist[neighbor]:
                    dist[neighbor] = dist_neighbor
                    prec[neighbor] = node
                    heappush(heap, (dist_neighbor, neighbor))
    return dist, prec




if __name__  == "__main__":
    _ = None
    G = [[1], [2], [5], [6], [3], [4, 8], [7], [4], [2]]
    W = [[ _, 1, _, 0, _, _, _, _, _],  # 0
         [ 1, _, 4, _, _, _, _, _, _],  # 1
         [ _, 4, _, _, _, 3, _, _, 2],  # 2
         [ 0, _, _, _, 1, _, 3, _, _],  # 3
         [ _, _, _, 1, _, 5, _, 1, _],  # 4
         [ _, _, 3, _, 5, _, _, _, 2],  # 5
         [ _, _, _, 3, _, _, _, 6, _],  # 6
         [ _, _, _, _, 1, _, 6, _, 2],  # 7
         [ _, _, 2, _, _, 2, _, 2, _],  # 8
        ]

    print(dijkstra(G, W))