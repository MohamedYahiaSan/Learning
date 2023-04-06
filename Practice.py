def grid(N,M):
    if N==0 or M==0: return 0
    
    dp=[[0 for _ in range (M+1) ] for _ in range (N+1)]
    dp[1][1]=1
    for i in range(1,N+1):
        for j in range(1,M+1):
           if i==1 or j==1:
               dp[i][j]=1
           else:
               dp[i][j]=dp[i][j-1]+dp[i-1][j] 
    
    return dp

print(*grid(18,18),sep='\n')