def long(txt,memo:dict={}):
    n=len(txt)
    
    if n==1: return 1
    if n==0: return 0
    if txt in memo: return memo[txt]
    
    count=0
    tmp_count=0
    
    
    for i in range(n):
        
        
        for j in range(i+1,n):
            if txt[i]==txt[j]:
                tmp_count=2+long(txt[i+1:j],memo)
            if tmp_count>count: count=tmp_count
        
    
    
    
    for i in range(n):
        for j in range(i+1,n):
            
    memo[txt]=count
    return count




txt="bbabcbcab"
txt2='bbabb'
print(long(txt2))