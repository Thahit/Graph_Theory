
def tsp(Graph: list, start: int):
    N = len(Graph)
    memo_table =[[None for _ in  range(2**N)] for _ in range(N)]
    #print(len(memo_table), len(memo_table[0]))
    
    def rec_combinations(set, at, r, n, subsets):
        if (n-at)<r:
            return
        if r==0:# base case
            subsets.append(set)
        else:
            for i in range(at, n):
                set |= (1<<i)# flip i'th bit
                rec_combinations(set, i+1, r-1, n, subsets)
                set &=  ~(1<<i)# flip back the bit
                #is like backtracking
        
    def combinations(r, n):
        subsets = []
        rec_combinations(0, 0, r, n, subsets)
        return subsets
    
    # setup
    for i in range(N):
        if i == start:
            continue
        # store optim. value from start to node i
        memo_table[i][(1 << start) | (1 << i)] = Graph[start][i]
        # the state == what is visited is saved in a single number, bit i stands for visiting city i
    # solve
    for r in range(3, N+1):# now we look at indirect paths
        for subset in combinations(r, N):
            if ((1 << start) & subset)==0:# useless subset== start not visited
                continue
            for next in range(N):
                if next == start or ((1 << next) & subset)==0:
                    continue
                state_without_next = subset ^(1<<next)# to check what was the best dist before visiting next
                min_dist = float("inf")
                for j in range(N):
                    if j == start or j == next or ((1 << j) & subset)==0:
                        continue
                    new_dist = memo_table[j][state_without_next] + Graph[j][next]# go to state then to next
                    if new_dist < min_dist:
                        min_dist = new_dist
                memo_table[next][subset] = min_dist
    
    # now we try to find the min cost
    end_state = (1<<N) -1 # = 1111111...
    min_cost = float("inf")
    for i in range(N):
        if i == start:
            continue
        cost = memo_table[i][end_state] + Graph[i][start]# go from the end of the tour back to the start
        if cost < min_cost:
            min_cost = cost
        
    # now we find the best path
    last_index = start
    state = end_state# could also recycle the var, but this is more readable
    path = [start]
    for i in range(1, N):# work yourself back from the end = range(N-1, 0, -1)
        best_index = -1
        best_dist = float("inf")
        for j in range(0, N):
            if j == start or ((1 << j) & state)==0:
                continue
            new_dist = memo_table[j][state] + Graph[j][last_index]
            if new_dist < best_dist:
                best_index = j
                best_dist = new_dist
        path.append(best_index)
        state ^= (1 << best_index)# new state = state before visiting index
        last_index = best_index
    path.append(start)
    return {"min_cost": min_cost, "path": path}
    

if __name__ == "__main__":
    # there are 3 examples you can test
    Graph = [[0, 1, 3, 4, 17, 11],# this graph is undirected-> needs to be symetric
             [1, 0, 2, 6, 2, 10],
             [3, 2, 0, 4, 7, 9],
             [4, 6, 4, 0, 6, 2],
             [17, 2, 7, 6, 0, 13],
             [11, 10, 9, 2, 13, 0],
             ]
    '''
    Graph = [[0, 4, 2, 6, ],# best sol from 0: 0->1->3->2->0 for 14
             [4, 0, 5, 2, ],
             [2, 5, 0, 6, ],
             [6, 2, 6, 0, ],
             ]
    '''
    '''
    Graph = [[10000 for _ in range(6)] for _ in range(6)]
    Graph[5][0] = 10
    Graph[1][5] = 12
    Graph[4][1] = 2
    Graph[2][4] = 4
    Graph[3][2] = 6
    Graph[0][3] = 8
    '''
    sol = tsp(Graph, 0)
    
    print("Cost of travel", sol["min_cost"])
    print("travelpath", sol["path"])
    