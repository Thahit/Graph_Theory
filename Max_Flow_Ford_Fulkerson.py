
def get_max_flow(graph: list, source: int, sink: int, n: int):
    #change graph into useful representations
    adj = [[0 for _ in range(n)] for _ in range(n)]
    for edge in graph:# we don't like the repr. we ger-> change to adj. matrix
        adj[edge[0]][edge[1]] = edge[2]
        
    def bfs(s, t, parent):# the algo itself does not specify how you get the paths but often stg. like dfs is used
        # we try to find paths from source to the sink
        visited = [False for _ in range(n)]
        q = []
        q.append(s)
        visited[s] = True
        
        while len(q):
            node = q.pop(0)
            
            for i in range(n):
                if visited[i] == False and adj[node][i] > 0:
                    q.append(i)
                    visited[i] = True
                    parent[i] = node
                    if i == t:
                        return True
                    
        return False
    
    parent = [-1 for _ in range(n)]
    max_flow = 0
    
    while bfs(source, sink, parent):# while there is a path from s to t (not fully used)
        path_flow = float("Inf")
        s = sink
        while(s !=  source):# work yourself back to the start
            path_flow = min (path_flow, adj[parent[s]][s])# find the bottleneck== the place where the least capacity is on the path
            s = parent[s]

        max_flow +=  path_flow

        v = sink
        while(v !=  source):
            # again starting from the sink, add vertices in the other direction, 
            # which make it possible to correct when you randonly seclected path was not the best
            u = parent[v]
            adj[u][v] -= path_flow
            adj[v][u] += path_flow
            v = parent[v]
    
    return max_flow

if __name__ == "__main__":
    # directed weighted graph
    
    n = 11
    s = n - 2# source
    t = n - 1# sink(somehow often named t)
    Graph = []# different falvour to create graph
    Graph.append((s, 1, 2))
    Graph.append((s, 2, 1))
    Graph.append((s, 0, 7))
    Graph.append((0, 3, 2))
    Graph.append((0, 4, 4))
    Graph.append((1, 4, 5))
    Graph.append((1, 5, 6))
    Graph.append((2, 3, 4))
    Graph.append((2, 7, 8))
    Graph.append((3, 6, 7))
    Graph.append((3, 7, 1))
    Graph.append((4, 5, 8))
    Graph.append((4, 8, 3))
    Graph.append((5, 8, 3))
    Graph.append((6, t, 1))
    Graph.append((7, t, 3))
    Graph.append((8, t, 4))
    
    '''
    n = 6
    s = n - 1
    t = n - 2
    Graph = []
    Graph.append((s, 0, 10))
    Graph.append((s, 1, 10))
    Graph.append((2, t, 10))
    Graph.append((3, t, 10))
    Graph.append((0, 1, 2))
    Graph.append((0, 2, 4))
    Graph.append((0, 3, 8))
    Graph.append((1, 3, 9))
    Graph.append((3, 2, 6))# sol = 19
    '''
    
    x = get_max_flow(Graph, s, t, n)
    print("max_flow: ", x)
    