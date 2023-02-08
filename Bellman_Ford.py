
def bellman_ford(graph: list, n: int, start :int):
    dist = [float("inf")] *n
    dist[start] = 0
    
    for _ in range(n):
        # traverse in random order(I just do them in order)
        for edge in graph:
            if dist[edge[0]] != float("inf") and dist[edge[0]] + edge[2] < dist[edge[1]]:
                dist[edge[1]] = dist[edge[0]] + edge[2]
                
    # now we have the cost if there were no (negative) cycles, but there might be some
    # check for negative cycles
    
    for _ in range(n):
        # traverse in random order(I just do them in order)
        for edge in graph:
            if dist[edge[0]] != float("inf") and dist[edge[0]] + edge[2] < dist[edge[1]]:
                dist[edge[1]] = float("-inf")# mark these with negative inf
                
    if float("-inf") in dist:
        print("Graph contains negative cycles.")
    
    return dist

if __name__ == "__main__":
    # need a directed graph (works with (negative) cycles):
    # I use a list of vertices(tuples) (source, dest, cost):
    Graph = [(0, 1, 4), (0, 2, 8), (1, 2, 7), (1, 3, 7),
            (3, 4, 2), (2, 4, 2), (4, 5, 6), (4, 6, 3),
            (4,7, -1), (7, 8, 17), (6,8, 4), (5, 9, 3),
            (8,6, -5), (5, 5, -1), # this part contains/produces neg. cycles
            ]
    n = 10# number of notes
    sol = bellman_ford(Graph, n, start = 0)
    print(sol, "\ninf stands for unreachable nodes, and -inf stands for nodes in/after an infinite negative loop.")

    