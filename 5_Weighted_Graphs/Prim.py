import heapq

def prim(adj, s):
    tree = [] # Edges we're going to take
    visited = set() # set of vertices we've seen in adj
    queue = [(0, s, s)]
    while queue:
        w, u, v = heapq.heappop(queue)
        if v in visited:
            continue
        visited.add(v)
        if u != v:
            tree.append((u,v))
        for neighbour, w in adj[v].items():
            if neighbour not in visited:
                heapq.heappush(queue, (w, v, neighbour))
    return tree


print(prim({
    0: {1: 1, 2: 4},
    1: {0: 1, 2: 2, 3: 6},
    2: {0: 4, 1: 2, 3: 3},
    3: {1: 6, 2: 3},
}, 0))