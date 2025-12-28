import functools

def bellman_ford(adj, s):
    @functools.cache
    def BF(v, k: int):
        if k == 0:
            return 0 if v == s else float('inf')
        else:
            predecessors = [u for u in adj if v in adj[u]]
            if not predecessors:
                return BF(v, k - 1)
            else:
                return min(BF(v, k - 1), min(BF(u, k - 1) + adj[u][v] for u in predecessors))

    dist = {}
    n = len(adj)
    for v in adj:
        dist[v] = BF(v, n - 1)
    return dist

print(bellman_ford({
    'A': {'B': 2, 'C': 4},
    'B': {'C': -2},
    'C': {}
}, 'A'))