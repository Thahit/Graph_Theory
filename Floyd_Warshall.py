
def floyd_warshall(Graph: list):
    # does not need a start, ut calculates the distances from, and to all nodes
    n = len(Graph)
    dist = [line for line in Graph]# just a copy
    # theoretically you use k arrays, but you can do the calculations in place
    
    for k in range(n):# visit k?
        for i in range(n):# pick source
            for j in range(n):# pick dest
                # check if it is faster to go via node k, or to reach your goal directly
                dist[i][j] = min(dist[i][j],
                                 dist[i][k]+dist[k][j])
    
    # similar to Bellman Ford, we can now find cycles by lokking at which distances still change
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = float("-inf")
    
    return dist

if __name__ == "__main__":
    # need a directed graph (works with (negative) cycles):
    #now a different form to represent Graphs:
    # an adj. matrix (inf weight = not connected)
    Graph = [[0, float("inf"), 3, 1, float("inf"), float("inf")],
             [float("inf"), 0, float("inf"), float("inf"), float("inf"), -2],
             [7, float("inf"), 0, 2, float("inf"), float("inf")],
             [1, float("inf"), float("inf"), 0, 4, float("inf")],
             [float("inf"), float("inf"), 3, -3, 0, float("inf")],
             [float("inf"), 1, float("inf"), float("inf"), float("inf"), 0],
             ]
    n = 6# number of notes(you can also get this from the graph)
    print("graph")
    for line in Graph:
        print(line)
    sol = floyd_warshall(Graph)
    print("solution")
    for line in sol:
        print(line)
    print("inf stands for unreachable nodes, and -inf stands for nodes in/after an infinite negative loop.")
