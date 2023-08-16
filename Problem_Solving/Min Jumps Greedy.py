# Solving Min Jumps using greedy approach

def greed(arr,n):
    
    if arr[0]==0: return -1
    if arr[0]>= n-1: return 1
    
    end=n-1
    current=0
    jumps=0
    
    while current<end:
        
        reachable=[i for i in range(current+1, min(n,current+arr[current]+1))]
        
        if not reachable:
            return -1
        
        
        jumps +=1
        
        temp=0
        maxx=0
        
        for i in reachable:
            cache= i+ arr[i]
            if cache>=end: return jumps+1
            
            if cache>maxx:
                maxx=cache
                temp=i
                
        current=temp
        
    return jumps
    

arr=[1,3,5,8,9,2,6,7,6,8,9,4,5,6,3,8,9,3,5,6,3]
n=len(arr)

print(greed(arr,n))                
        