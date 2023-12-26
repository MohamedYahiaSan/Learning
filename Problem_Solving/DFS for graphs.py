#DFS for graphs
def DFS(V,adj):
    cache={}
    visited=set() #Set to store visited Vortexes
    result=[] #Results

    #Initializing a dictionary for the graph
    for i in range(V):
        cache[i]=adj[i]
    
    #Recursive function to go through the vertexes
    def recur(visited,current):
        if current in visited:
            return []
        
        visited.add(current)
        result.append(current)

        for ele in cache[current]:
            recur(visited,ele) #Going through the votexes by turn 

    recur(visited,0)

    return result

#Simple text examples
V_0=5
adj_0=[[2,3,1] , [0], [0,4], [0], [2]]
V_1=4
adj_1=[[1,3], [2,0], [1], [0]]
V_2=5
adj_2=[[1,2,3],[0,2],[0,1],[0,4],[3]]

A=DFS(V_0,adj_0)
print(A)
B=DFS(V_1,adj_1)
print(B)
C=DFS(V_2,adj_2)
print(C)