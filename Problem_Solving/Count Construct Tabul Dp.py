def can(s,arr):
    N=len(s)
    M=len(arr)
    
    
    dp=[0 for _ in range(N+1)]
    dp[0]=1

    for i in range(0,N+1):
       if dp[i]>0:
           for ele in arr:
               if ele in s:
                le=len(ele)
                if s[i:i+le] == ele and i+le <N+1:
                    dp[i+le]+=dp[i]
                        
     
            
    return dp

#print(can("abcdef",['ab','abc','cd','def','abcd','abcdef']))
#print(can('mohamed yahia',['ia','ah',' y','moha','med','mohame','d yahia']))
print(can('enterapotentpot',['a','p','ent','enter','ot','o','t']))
#print(can("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",['e','eeee','eeeeeeeee','ee']))