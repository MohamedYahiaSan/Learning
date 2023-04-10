def How(N,arr,mem={}):
    if N in mem: return mem[N]
    if N in arr: return [N]
    if N == 0: return []
    if N< 0 : return []
    
   
    
    for n in arr:
        result=How(N-n,arr,mem)
        if len(result)>0: 
            mem[N]=result+[n]
            
            return mem[N]
    mem[N]=[]
    return mem[N] 


print(How(300,[105,15]),'---------------', sep='\n')

def Thow(N,arr):
    if N in arr: return [N]
    if N == 0: return []
    if N< 0 : return None
    
    dp=[[]]*(N+1)
    dp[0]=True
    

    for i in range(1,len(dp)):
        
        if i in arr:
            dp[i]=[i]
                
        for j in arr:
            if i+j <=N and dp[i]:
                dp[i+j]=dp[i]+[j]
                
                
    print(dp[-1])

    
Thow(300,[150,1000])