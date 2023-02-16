from queue import PriorityQueue

def prims_MST(graph: list, starting_node: int = 0):
    n = len(graph)
    visited = [False for _ in range(n)]
    m = n -1 # number of edges required
    edge_count = mst_cost = 0
    mst_edges = [None for _ in range(m)]
    prioq = PriorityQueue()
    
    def add_edges(node):
        visited[node] = True
        for edge in range(n):
            if graph[node][edge] != float("inf") and not visited[edge]:
                prioq.put((graph[node][edge], node, edge))# == cost, from, to
    
    add_edges(starting_node)
    
    while not prioq.empty() and m>0:
        edge = prioq.get()
        node_index = edge[2]#to
        
        if visited[node_index]:
            continue
        mst_edges[edge_count] = edge
        edge_count += 1
        mst_cost += edge[0]# cost
        add_edges(node_index)
    
    if edge_count !=m:# no mst exists
        return (None, None)
    
    return (mst_edges, mst_cost)

if __name__ == "__main__":
    # undirected weighted graph
    '''
    Graph = [[0, -1, 3, float("inf"), float("inf"), 4],# this graph is undirected-> needs to be symetric
             [-1, 0, 2, float("inf"), 2, float("inf")],
             [3, 2, 0, float("inf"), float("inf"), float("inf")],
             [float("inf"), float("inf"), float("inf"), 0, 6, 2],
             [float("inf"), 2, float("inf"), 6, 0, 17],
             [4, float("inf"), float("inf"), 2, 17, 0],
             ]#edges:  [(-1, 0, 1), (2, 1, 2), (2, 1, 4), (4, 0, 5), (2, 5, 3)] cost:  9
    '''
    Graph = [[0, 2, 5, 2, 3, float("inf")],# this graph is undirected-> needs to be symetric
             [2, 0, float("inf"), 0, float("inf"), float("inf")],
             [5, float("inf"), 0, 1, 6, float("inf")],
             [2, 0, 1, 0, 4, 8],
             [3, float("inf"), 6, 4, 0, float("inf")],
             [float("inf"), float("inf"), float("inf"), 8, float("inf"), 0],
             ]# cost = 14, edges = [(2, 0, 1), (0, 1, 3), (1, 3, 2), (3, 0, 4), (8, 3, 5)]
    
    x = prims_MST(Graph)
    print("edges: ")
    for edge in x[0]:
        print("from: ",edge[1] , "to: ",edge[2] , "cost: ", edge[0])
    print("cost: ", x[1])
