# Solving Min Jumps using Recur

def recur(arr,n,mem={}):
    global memo 
    memo=mem 
    if arr[0]==0: return float('inf')
    
    if n in mem:
        return mem[n]
    
    if arr[0]>= n-1: return 1
    else:
        x=arr[0]
    counter=0
    mini=float('inf')
    
    for i in range(1,x+1):
        counter=1+ recur(arr[i:],n-i,mem)
        if counter<mini:
            mini=counter
            
    mem[n]=mini
    return mini


arr=[1,3,5,8,9,2,6,7,6,8,9,4,5,6,3,8,9,3,5,6,3]
n=len(arr)

print(recur(arr,n),memo,sep='\n')


# Solving Min Jumps using Tabulation
def tab(arr,n):
    if arr[0]==0: return -1
    
    dp=[float('inf') for _ in range(n)]
    # -1 means not visited yet, or 0.
    dp[-1]=0
    
    for i in range(n-2,-1,-1):
    
        if arr[i]==0:
            continue
        
        if i+arr[i]<n-1:
            
            if any(dp[i+1:i+arr[i]+1])!= float('inf'):
                dp[i]=1+min(dp[i+1:i+arr[i]+1]) 
        
        
        else:
            
            if any(dp[i+1:])!= float('inf'):
                dp[i]=1+min(dp[i+1:]) 

     
    print(dp)
    return dp[0]



arr2=[2,3,1,1,2,4,2,0,1,1]
n2=len(arr2)
print(tab(arr,n))
