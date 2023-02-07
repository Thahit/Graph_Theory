from Topological_Sort import top_sort

def dag_sortest_path(graph: list, n: int, start :int):
    ordering = top_sort(graph, n)# for sthis algo. we need a topological order
    distances = [None for _ in range(n)]# None = not found/connected = infinite dist
    distances[start] = 0
    
    for i in range(n):
        #current_node = distances[i]
        if(distances[i] != None):# == reachable
            for edge in graph:# find connected nodes
                if edge[0] == i:
                    if distances[edge[1]] != None:
                        distances[edge[1]] = min(distances[edge[1]], distances[i] + edge[2])
                    else:# dist was still None
                        distances[edge[1]] = distances[i] + edge[2]
    
    return distances
    
if __name__ == "__main__":
    # need a directed graph without cycle:
    # I use a list of vertices(tuples) (source, dest, cost):
    Graph = [(0, 1, 4), (0, 2, 8), (1, 2, 7), (1, 3, 7),
            (3, 4, 2), (2, 4, 2), (4, 5, 6), (4, 6, 3),
            (4,7, -1), (7, 8, 17), (6,8, 4)]
    n = 9
    # goal: get an array with the cost to all paths
    sol = dag_sortest_path(Graph, n, start = 2)
    print(sol)
    # for max path, multiply costs with -1
