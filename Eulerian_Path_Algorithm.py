
def eulerian_path(graph: list, n: int):
    in_count = [0 for _ in range(n)]
    out_count = [0 for _ in range(n)]
    path = []
    
    def dfs(at):
        # sligtly strang way th write it, I woud leave out the while but I want to be closer to the source i found
        while(out_count[at] != 0):
            # take edge and remove it
            # a better representation for the graph would be useful here
            for edge in range(len(graph)):
                if graph[edge][0] == at:
                    next = graph[edge][1]
                    print("visiting", next)
                    # edge has been visited so
                    # del graph[edge] # delete or
                    graph[edge] = (-1, -1) # make useless/mark
                    out_count[at] -= 1
                    dfs(next)
                    break
        
        path.insert(0, at)
    
    # count in and outgoing edges
    for edge in graph:
        in_count[edge[1]] += 1
        out_count[edge[0]] += 1
        
    # check if path exists:
    nr_start_nodes = nr_end_nodes = 0
    start = -1
    for i in range(n):
        if (out_count[i]- in_count[i]) > 1 or (in_count[i]- out_count[i])>1:
            # == a node as too many incomming/outgoing edges == you get stuck/cannot reenter
            print("no Eulerian path possible")
            return None
        elif (out_count[i]- in_count[i])==1:#==you have one more outgoing-> you need to start here
            nr_start_nodes += 1
            start = i# so if there is a node where we have to start, we take this one, see below
        elif (in_count[i]- out_count[i])==1:#==you have one more incomming-> you need to end here
            nr_end_nodes += 1
    if not ((nr_start_nodes == 0 and nr_end_nodes == 0) or (nr_start_nodes == 1 and nr_end_nodes == 1)):
        # need either no start(so start anywhere) or exactly one(and corresponding number of end nodes)
        print("no Eulerian path possible")
        return None     
    
    if start ==-1:# no start selected-> take one note whith an outgoing edge
        for i in range(n):
            if out_count[i]:
                start = i
                break
        
    print("starting node: ", start)
    
    # dfs from start
    dfs(start)
    
    if len(path) == len(graph)+1:# all edges used
        return path
    
    print("no Eulerian path possible")
    return None

if __name__ == "__main__":
    # there are versions for directed and undirected graphs
    # This code will be for undirected graphs
    #list of edges(source, dest), (no cost required)
    Graph = [(1, 2), (1, 3), (2, 2),# as you can see, node 0 is not connected to anything, which is not a problem
             (2, 4), (2, 4), (3, 1),
             (3, 2), (3, 5), (4, 3),
             (4, 6), (5, 6), (6, 3),# you can try changing the edges,
             ]# the/one solution for this graph is [1, 2, 2, 4, 3, 1, 3, 2, 4, 6, 3, 5, 6]
    n = 7# nr. of nodes
    x = eulerian_path(Graph, n)
    print("path: ", x)