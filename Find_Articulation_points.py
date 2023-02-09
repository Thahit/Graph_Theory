
def find_bridges(Graph: list):
    # I don't know if this algo. has a special name
    # it is very similar to the find bridges algo(due to the similarities in the tasks)
    index = [None] * len(Graph)
    low_link = [None] * len(Graph)
    is_art = [False] * len(Graph)
    
    idx = [0]# stupid way to take it with me :( python
    
    # unfortunately this one is not as readable
    def dfs(at, parent, root):
        if parent==root:
            out_edge_count[0]+=1
        low_link[at] = index[at] = idx[0]
        idx[0] += 1
        for to in range(len(Graph)):
            if Graph[at][to] != float("inf") and to != parent and to != at:# if connected+ not parent
                if index[to] == None:# not visited
                    dfs(to, at, root)
                    low_link[at] = min(low_link[at], low_link[to])
                    if low_link[at]<= low_link[to]:
                        # if < then it is because of the bridge
                        # if = then cycle
                        is_art[at] = True
                        # this means you child never got a way back to  you-> you are the only connection-> bridge
                else:
                    low_link[at] = min(low_link[at], low_link[to])
    
    # dfs from random start:(I just start at node 0)
    while None in index:
        # if not all nodes are connected->there is several subgraphs, we need several restarts
        random_start = index.index(None)
        out_edge_count = [0]
        dfs(random_start, -1, random_start)
        is_art[random_start] = out_edge_count[0]>1
    
    return is_art

if __name__ == "__main__":
    # need an undirected graph (works with (negative) cycles):
    # an adj. matrix (inf weight = not connected)
    Graph = [[0, -1, 3, float("inf"), float("inf"), float("inf")],# this graph is undirected-> needs to be symetric
             [-1, 0, 2, float("inf"), 2, float("inf")],
             [3, 2, 0, float("inf"), float("inf"), float("inf")],
             [float("inf"), float("inf"), float("inf"), 0, 6, 2],
             [float("inf"), 2, float("inf"), 6, 0, float("inf")],
             [float("inf"), float("inf"), float("inf"), 2, float("inf"), 0],
             ]
    n = 6# number of notes(you can also get this from the graph)

    sol = find_bridges(Graph)
    print(sol)
    
