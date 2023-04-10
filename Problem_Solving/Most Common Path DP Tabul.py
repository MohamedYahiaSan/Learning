def com(stack1,stack2):
    
    N=len(stack1)
    M=len(stack2)
    
    if M == 0 or N ==0 : 
        return 0
    
    dp=[[0 for _ in range(N+1)] for _ in range(N+1)]
    print(*dp,sep='\n',end='\n\n')
    
    for i in range(1,N+1):
        for j in range(1,M+1):
                       
            if stack1[i-1]==stack2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp

print(*com([2,7,1,15,15,9,6,14,15,10],[1,6,14,15,15,15,7,9,2,10]),sep='\n')   