
def find_bridges(Graph: list):
    # I don't know if this algo. has a special name
    index = [None] * len(Graph)
    low_link = [None] * len(Graph)
    bridges = []
    
    idx = [0]# stupid way to take it with me :( python
    
    # unfortunately this one is not as readable
    def dfs(at, parent):
        low_link[at] = index[at] = idx[0]
        idx[0] += 1
        for to in range(len(Graph)):
            if Graph[at][to] != float("inf") and to != parent and to != at:# if connected+ not parent
                if index[to] == None:# not visited
                    dfs(to, at)
                    low_link[at] = min(low_link[at], low_link[to])
                    if low_link[at]< low_link[to]:
                        # this means you child never got a way back to  you-> you are the only connection-> bridge
                        bridges.append((at, to))
                else:
                    low_link[at] = min(low_link[at], low_link[to])
    
    # dfs from random start:(I just start at node 0)
    while None in index:
        # if not all nodes are connected->there is several subgraphs, we need several restarts
        random_start = index.index(None)
        dfs(random_start, -1)
    
    return bridges

if __name__ == "__main__":
    # need a directed graph (works with (negative) cycles):
    #now a different form to represent Graphs:
    # an adj. matrix (inf weight = not connected)
    Graph = [[2, -1, 3, float("inf"), float("inf"), float("inf")],# this graph is undirected-> needs to be symetric
             [-1, 0, 2, float("inf"), 2, float("inf")],
             [3, 2, 0, float("inf"), float("inf"), float("inf")],
             [float("inf"), float("inf"), float("inf"), 0, 6, 2],
             [float("inf"), 2, float("inf"), 6, 0, float("inf")],
             [float("inf"), float("inf"), float("inf"), float("inf"), 2, 0],
             ]
    n = 6# number of notes(you can also get this from the graph)

    sol = find_bridges(Graph)
    print(sol)
    
