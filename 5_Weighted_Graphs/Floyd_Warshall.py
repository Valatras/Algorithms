import functools

def floyd_warshall(adj: dict):        
    
    @functools.cache
    # u, v, k == point1, point2, nombre de point intermédiaire
    def FW(u, v, k):
        if k == 0:
            return adj.get(u, {}).get(v, float('inf'))
        else:
            # Get the list of vertices for the k-th intermediate node
            vertices = list(adj.keys())
            intermediate = vertices[k - 1]
            return min(
                FW(u, v, k - 1),
                FW(u, intermediate, k - 1) + FW(intermediate, v, k - 1)
            )
        
    vertices = list(adj.keys())
    n = len(vertices)

    # Build all-pairs distance dictionary using the cached FW
    result = {u: {} for u in vertices}
    for u in vertices:
        for v in vertices:
            result[u][v] = FW(u, v, n)

    # Ensure zero on the diagonal unless a negative cycle exists
    for v in vertices:
        result[v][v] = min(result[v][v], 0)

    # Detect negative cycles
    for v in vertices:
        if result[v][v] < 0:
            print("Negative cycle detected")
            break
    else:
        # Pretty-print the distance matrix
        print("All-pairs shortest paths:")
        for u in vertices:
            row = []
            for v in vertices:
                val = result[u][v]
                row.append("∞" if val == float('inf') else str(val))
            print(f"{u}: {', '.join(row)}")

    return result

floyd_warshall({
    'A': {'B': 2, 'C': 4},
    'B': {'C': -2},
    'C': {}
})