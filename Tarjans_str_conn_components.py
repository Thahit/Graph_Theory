
def Tscc(graph: list, n: int):
    index = [-1] * n# -1 functions also as "not visited"
    low_link = [-1] * n# same as before: index of earliest visitable node
    stack_member = [False] * n
    connected = []
    stack = []
    idx = [0]
    
    def dfs(at):
        stack.append(at)
        stack_member[at] = True
        low_link[at] = index[at] = idx[0]
        idx[0] +=1
        
        for edge in graph:# not the best graph representation for this kind of graph
            if edge[0] == at:
                if index[edge[1]]==-1:
                    dfs(edge[1])
                if stack_member[edge[1]]:
                    low_link[at] = min(low_link[at], low_link[edge[1]])
                    
        if index[at] == low_link[at]:
            scc = []
            while len(stack):
                current = stack.pop()
                stack_member[current] = False
                scc.append(current)
                low_link[current] = low_link[at]
                if current == at:
                    connected.append(scc)
                    break
                

    # Call the recursive helper function
    # to find articulation points
    # in DFS tree rooted with vertex 'i'
    for i in range(n):
        if index[i] == -1:# not jet visited
            dfs(i)

    return connected

if __name__ == "__main__":
    # find strongly connected components
    Graph = [(0, 1), (1, 2), (2, 0), (2, 3),
            (3, 4), (4, 5), (5, 6), (5, 4),
            (6, 3), (4, 7), (7, 8), (8, 9), (9,8)]# sol:(0,1,2), (3,4,5,6), (7), (8,9)
    n = 10# number of notes
    sol = Tscc(Graph, n)
    print(sol)
