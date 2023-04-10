def can(s,arr):
    
    N=len(s)
    M=len(arr)
    if N==0 : return [[]]
    if M==0 : return [[]]
    dp=[[] for _ in range(N+1)]
    dp[0]=[[]]
   
    for i in range(N+1):
        if  len(dp[i])>0:
            for ele in arr:
                if ele == s[i:i+len(ele)] and i+len(ele)<N+1:
                    dp[i+len(ele)]+=[x+[ele] for x in dp[i]]
            
    
   

    return dp[-1]
        

print(can("abcdef",['ab','abc','cd','def','abcd','ef','c']))
#print(can('mohamed yahia',['ia','ah',' y','moha','med','mohamed']))
#print(can("eeeeeeeeeeee",['e','eeee','f','eeeeeeeee','ee']))