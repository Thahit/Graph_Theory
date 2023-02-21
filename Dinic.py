
def get_max_flow(graph: list, source: int, sink: int, n: int):# another way to get the max flow: dinics algo.
    #change graph into useful representations
    if sink==source:
        return -1
    adj = [[] for _ in range(n)]
    # flow, capacity  (maybe this representation is more readable than the last one one)
    level = [-1 for _ in range(n)]# the level of the nodes in the current graph, higher level->closer to goal/sink
    for edge in graph:# we don't like the repr. we ger-> change to adj. matrix
        adj[edge[0]].append([edge[1], 0, edge[2], len(adj[edge[1]])])# dest, flow, capacity, idx of back edge
        adj[edge[1]].append([edge[0], 0, 0, len(adj[edge[0]])])# same for back edge
        
    def bfs(s, t):# the algo itself does not specify how you get the paths but often stg. like dfs is used
        # we try to find paths from source to the sink
        for i in range(n):
            level[i] = -1
        q = []
        q.append(s)
        level[s] = 0
        
        while len(q):
            node = q.pop(0)
            
            for edge in adj[node]:
                if level[edge[0]] == -1 and edge[2] > edge[1]:# not visited and free capacity
                    q.append(edge[0])
                    level[edge[0]] = level[node] + 1
                    
        return level[t] > -1 #sink reached
    
    def sendFlow(current, flow, t):#, start
        # Sink reached
        if current == t:
            return flow

        idx = 0
        
        #while start[current] < len(adj[current]):# go over all edges
        while idx < len(adj[current]):# go over all edges
            
            #e = adj[current][start[current]]#connected edge
            e = adj[current][idx]#connected edge
            if level[e[0]] == level[current] + 1 and e[1] < e[2]:# free flow available and on next level
 
                # find minimum flow
                curr_flow = min(flow, e[2]-e[1])# update bottleneck with minimum free capacity
                temp_flow = sendFlow(e[0], curr_flow, t)# , start
 
                if temp_flow and temp_flow > 0:
                    e[1] += temp_flow

                    adj[e[0]][e[3]][1] -= temp_flow # subtract frlow of back-edge
                    return temp_flow
            #start[current] += 1
            idx += 1
 
    max_flow = 0
    
    while bfs(s, t):
        # start = [0 for _ in range(n + 1)]
        # the version I saw used this start array but I don't see the purpose of it
        # the fragments of it are still there in case someone is interested / if there is a reason for it, the code can be recovered
        # but I think the version with idx is more efficient 
        
        while True:
            flow = sendFlow(s, float('inf'), t) # , start
            
            # see if there is still capacity in the current graph
            if not flow:
                break

            # Add path flow to overall flow
            max_flow += flow   
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
    