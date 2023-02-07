import random

def top_sort(graph: list, n: int):
    def dfs(node: int):
        for edge in graph:# could delete used edges
            if node == edge[0] and not visited[edge[1]]:
                dfs(edge[1])
        visited[node] = True
        solution.insert(0, node)
        
    solution = []
    visited = [False for _ in range(n)]
    
    while False in visited:# not all visited
        # pick random starting node 
        # (picking the beginning would be better here but we should not know that)
        start = random.randint(0, n-1)
        if visited[start]:# random node was already visited
            # (I don't want to search smarter,
            # because the problem is easy)
            continue
        dfs(start)
    return solution

if __name__ == "__main__":
    # need a directed graph without cycle:
    # I use a list of vertices(tuples) (source, dest):
    Graph = [(0, 1), (0, 2), (1, 2), (1, 3),
            (3, 4), (2, 4), (4, 5), (4, 6),
            (4, 7), (7, 8), (6, 8)]# sol has to start with 0 and end with 5 or 8
    n = 9# number of notes
    # the goal is to sort the nodes in a way that:
    # no dest. is in the list in front of its source
    # for example you cannot take math 2 before having taken math1
    sol = top_sort(Graph, n)
    print(sol)
    # there is not allways an unique solution,
    # so running the skript again might show a different one
    