#create and populate a tree from entries, also find distance between any values/nodes
from collections import defaultdict as dd



Tree_nodes=dd(list)                                         #Tree Map (will be used to create Tree nodes)
nodes_parent=dd(int)                                        #Map the parent of each node with values only

# Reading data and assiging them to vars to use (using a file for large entries)
file=open('data.txt','r')                               
n = int(file.readline())
for _ in range(n-1):
    read=(list(map(int,file.readline().split())))
    i,j=min(read),max(read)
    Tree_nodes[i].append(j)
    nodes_parent[j]=i
file.close()



# Def Class for Nodes in the tree
class Node:
    # Class variable for distance between node/value storage
    distance={}
    value_distance={}
    Node_name=dd(int)

    # Initializing with some helpful node info
    def __init__(self,data,kids=[],level=0,parent=None):
        self.data=data
        self.kids=kids
        self.level=level
        self.parent=parent
        self.sets=[]
        self.grands={}

    #Method to fill a tree with nodes from Tree_nodes dictionary (Static Method) and return the head
    def Filler(Tree:dict):
        head=Node(1,Tree[1],0)
        Node.Node_name[1]=head
        curr=head
        def kid_fill(curr):
            for i in range(len(curr.kids)):
                curr.kids[i]=Node(curr.kids[i],Tree[curr.kids[i]],curr.level+1,curr)
                curr.kids[i].grands[curr]=1
                curr.kids[i].grands.update({gran:lv+1 for gran, lv in curr.grands.items()})
                Node.Node_name[curr.kids[i].data]=curr.kids[i]
                kid_fill(curr.kids[i])
        kid_fill(curr)
        return head
    
    # Just for representation
    def __repr__(self) -> str:
        #return f'Node Data:{self.data} , Kids:{list(map(lambda x: x.data,self.kids))}, Level:{self.level}'
        return f'{self.data}'

    # Distance between nodes using the tree structure  returns the distance as int 
    def node_dist(self,node1,node2):
        a,b=sorted([node1,node2],key=lambda x:x.data)
        if (a,b) in self.distance:
                return self.distance[(a,b)]
        
        while True:
            if a==b:
                temp_dist=node1.level+node2.level-a.level-b.level
                self.distance[tuple(sorted([node1,node2],key=lambda x:x.data))]=temp_dist
                return temp_dist

            if (a,b) in self.distance:
                temp_dist=self.distance[(a,b)]+node1.level+node2.level-a.level-b.level
                self.distance[tuple(sorted([node1,node2],key=lambda x:x.data))]=temp_dist
                return temp_dist
            
            
            if a.level>b.level:
                a=a.parent
                continue
            else:
                b=b.parent
                continue
        
    
    #Func to map the distance between all possible node/value pairs using tree structre
    def value_dist(self,head):
        stack=[head]
        while stack:

            curr=stack.pop(0)
            stack+=curr.kids

            queue=[head]
            while queue:
                q=queue.pop(0)
                queue+=q.kids

                a,b=sorted([curr,q],key= lambda x:x.data)
                if (a.data,b.data) in self.value_distance:
                    continue
                else:
                    self.value_distance[(a.data,b.data)]=self.node_dist(a,b)
    
    #Creating a Dynamic Programming Distance Map using Dictionaries made while reading (Static Method)
    def dp_map(nodes_parent,Tree_nodes,n):
        dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if nodes_parent[j]==i:
                    dp[i][j]=1
                    continue
                elif i in Tree_nodes[nodes_parent[j]]:
                    dp[i][j]=2
                    continue
                else:
                    a,b=min(i,nodes_parent[j]),max(i,nodes_parent[j])
                    
                    dp[i][j]=1+dp[a][b]
        
        return dp

    #calculating distance from stored LCA
    def grands_distance(n1,n2):

        n2,n1=sorted([n1,n2],key=lambda x:x.data)
        if n2 == n1: return 0
        elif n2 in n1.grands:
            return n1.grands[n2]
        
        for g1,d1 in n1.grands.items():
            if g1 in n2.grands:
                return ( d1+n2.grands[g1])


            

#Initializing our Tree with head Node
head =Node.Filler(Tree_nodes)
head.value_dist(head)
print('-----------------------')
# print(head.distance)
# print(head.value_distance)
dp=Node.dp_map(nodes_parent,Tree_nodes,n)
print(*dp,sep='\n')











