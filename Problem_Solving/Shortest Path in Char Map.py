'''
Problem: Reach from S to F in Shortest path through '.' only and print path in '|'
Char Map: txt
'''
#Char Map
txt=[
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXX.........SXXXXXXXXXXXXXXXXXXX",
    "XX.X.....XXXXXXX.....XXXXXXXXXXX",
    "XX....XXXXXXXXXX.XXX.XX.....XXXX",
    "XXXXX..XXXXXX....XXX.XX.XXX.XXXX",
    "XXX.XX.XXXXXX.XX.XXX.XX..XX.XXXX",
    "XXX.....XXXXX.XXXXXX.XXXXXX.XXXX",
    "XXXXXXX.......XXXXXX........XXXX",
    "XXXXXXXXXX.XXXXX.XXXXXXXXXX.XXXX",
    "XXXXXXXXXX.XX....XXXXX......XXXX",
    "XXXXXXXXXX....XXXXXXXX.XXXX.XXXX",
    "XXXXXXXXXXX.XXXXXXXXXX.XXXX.XXXX",
    "XXXXXXXXXXX.....XX.....XXXX.XXXX",
    "XXXXXXXXXXXX.XXXXXXXXXXX.XX.XXXX",
    "XXXXXX........X.....XXXX.XX.XXXX",
    "XXXXXX.XX.XXXXXXXXX.XX......XXXX",
    "XXXXXX.XXF...XXXXXX.XXXX.XXXXXXX",
    "XXXXXX.XXXXX...XXX............XX",
    "XXXXXX.XXXXXXX.XXXXXXXXXXX.XX.XX",
    "XXXXXX.XXXXXXX.XXXXXXXXXXXXXX.XX",
    "XXXXXX...XXX..................XX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

#Reading the dimensions
height=len(txt)
width=len(txt[0])

#Creating a node class to traverse the map
class node:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.adjacent=[]
        self.visited = set()
        self.path=[]

#Transfroming opening slots into nodes and reading the start and goal 
nodes={}
for i in range(height):
    for j in range(width):
       if txt[i][j] == '.': nodes[(i,j)]=node(i,j)
       if txt[i][j] == 'S': start=(i,j)
       if txt[i][j] == 'F': goal=(i,j)

#Filling adjacent nodes for each node
for item in nodes.values():
    x=item.i 
    y=item.j
    if (x-1,y) in nodes: item.adjacent.append(nodes[(x-1,y)])
    if (x+1,y) in nodes: item.adjacent.append(nodes[(x+1,y)])
    if (x,y-1) in nodes: item.adjacent.append(nodes[(x,y-1)])
    if (x,y+1) in nodes: item.adjacent.append(nodes[(x,y+1)])

#Check if the node is adjacent to the goal
def arrived(n,goal):
    if abs(n.i-goal[0])==1 and abs(n.j-goal[1])==0: return True
    elif  abs(n.i-goal[0])==0 and abs(n.j-goal[1])==1: return True
    else: return False

#Locating the starting node (any node adjacent to the start)
def start_node(start, nodes):
    if  (start[0]-1,start[1]) in nodes: return nodes[(start[0]-1,start[1])]
    elif  (start[0]+1,start[1]) in nodes: return nodes[(start[0]+1,start[1])]
    elif   (start[0],start[1]-1) in nodes: return nodes[(start[0],start[1]-1)]
    else: return nodes[(start[0],start[1]+1)]


#Initializing the traversal based on visited nodes and saving  the path till each node from the start
queue=[start_node(start,nodes)]             #Starting node in the queue
path=[]                                     #Paths from start to goal

while True:                                 #Traversing the map
    if queue==[]: break                     #Break condition
    n=queue.pop()
    
    if arrived(n,goal):                     #Check for arrival
        n.path.append((n.i,n.j))
        path.append(n.path)
        print('arrived')

    for ele in n.adjacent:                  #Updating the queue and the path for new nodes
        if not ele in n.visited: 
            ele.visited=n.visited.copy()
            ele.visited.add(n)
            #The below section is to make sure each node only stores the shorted path from start untill arrival at self
            if ele.path== []: ele.path=n.path+[(n.i,n.j)]
            else: 
                if len(ele.path)<len(n.path+[(n.i,n.j)]): pass
                else: ele.path=n.path+[(n.i,n.j)]
            queue.append(ele)

#Choosing the shortest path
path=sorted(path, key= lambda x:  len(x))

#Printing the new map
n_txt=[list(x) for x in txt]               #Creating a list of the Char map

for ele in path[0]:                        #Replacing the shortest path with '|'
    n_txt[ele[0]][ele[1]]='|'

n_txt= ["".join(x) for x in n_txt]         #Reconstructing the strings

#Printing the map with the shortest path
print(*n_txt, sep='\n')