# Longest common palindromic subsequence function
def pali(txt):
    n=len(txt)
    
    # Initialzing the dp 2D array
    dp=[[0 for i in range(n)] for j in range(n)]
    
    # Filling the diagonal
    for i in range(n):
        dp[i][i]=1
    

    # Start cells
    x=1
    i=0
    j=i+x
    
    
    # Filling the array after the diagonal
    while True:
        if txt[i]==txt[j]:
            dp[i][j]=2+dp[i+1][j-1]
        else:
            dp[i][j]= max(dp[i][j-1],dp[i+1][j])
        
        if i==0 and j==n-1:
            break
        
        if j== n-1:
            i=0
            x+=1
            j=i+x
        else:
            i+=1
            j+=1
        
               
    print(*dp,sep='\n')
    return dp[0][n-1]

# Testing
txt='babcbcab'  
print(pali(txt))