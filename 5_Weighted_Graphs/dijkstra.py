import heapq

def dijkstra(adj, start):
    # BFS, to change so that it uses a priority queue
    # adj is a dict of dicts, representing the paths and their weights
    dist = {u: 0 if start == u else float('inf') for u in adj} # infinite distance initially from start to all nodes
    queue = [(0, start)]  # priority queue of (distance, node), 
    # it means that we will always explore the node with the smallest distance first
    
    while queue:

        node = heapq.heappop(queue)[1]
        for neighbour, weight in adj[node].items():

            print("Current node : ", node)
            print(neighbour, " weights : ", weight)
            if dist[node] + weight < dist[neighbour]: # si infini + weight < infini
                
                print(dist[node] + weight, " < ", dist[neighbour], "\n")
                dist[neighbour] = dist[node] + weight
                heapq.heappush(queue, (dist[neighbour], neighbour))


        # version de base BFS
        # node = queue.pop(0)
        # for neighbour in adj[node]:
        #     if neighbour not in dist:
        #         dist[neighbour] = dist[node] + 1
        #         queue.append(neighbour)

    return dist

search = dijkstra({
    'A': {'B': 4, 'C': 1},
    'B': {},
    'C': {'B': 2}
}, 'A')

print(search)
