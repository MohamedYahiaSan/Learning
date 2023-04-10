def Best(N,arr,mem={}):
    if N in mem: return mem[N]
    if N==0: return []
    if N<0: 
        return None
    
    result=[]
    
    for ele in arr:
        
        x= Best(N-ele,arr,mem)
        if x!= None:
            x=x+[ele]
            if len(x)< len(result) or result==[]: 
                result=x
            
             
        else: continue
    mem[N]=result        
        
          
    return mem[N]   
    
#print(Best(8,[5,33,7,1]))


def Tbest(N,arr):
    if N==0 : return []
    if N<0: return None
    
    M=N+1
    dp=[[0]]*M
    dp[0]=[]
    
    for i in range(1,M):
        for j in arr:
            if i in arr:
                dp[i]=[i]
            if dp[i]!=[] and i+j<M:
                if dp[i+j]==[0]: dp[i+j]=[j] +dp[i]
                if len(dp[i+j])>len([j] +dp[i]): dp[i+j]=[j] +dp[i]
            
    return (dp[-1])

print(Tbest(100,[5,25,1,2]))
        