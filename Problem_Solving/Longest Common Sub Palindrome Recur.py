# Function to find the longest common subsequence inside a single text
def long(txt,memo:dict={}):
    n=len(txt)
    
    # Base Cases with Memoization (Actually memoization have no ned)
    if n==1: return 1
    if n==0: return 0
    if txt in memo: return memo[txt]
    
    # Initializing counters
    count=0
    tmp_count=0
    
    # Recursion
    for i in range(n):
        for j in range(i+1,n):
            if txt[i]==txt[j]:
                tmp_count=2+long(txt[i+1:j],memo)
            if tmp_count>count: count=tmp_count
        
    # Memo and output   
    memo[txt]=count
    return count

    


txt="bbabcbcab"
txt2='bxcab'
print(long(txt2))