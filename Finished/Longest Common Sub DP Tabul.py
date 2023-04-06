def lcs(s,t):
    N=len(s)
    M=len(t)
    
    if M==0 or N==0: return  0
    
    dp=[[0 for _ in range(N+1)] for _ in range(M+1)]

    for i in range(1,M+1):
        for j in range(1,N+1):
            
            if t[i-1]==s[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
                
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp


print(*lcs("AGGTAB","GXTXAYB"),sep='\n')
