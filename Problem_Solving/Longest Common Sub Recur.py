def lcs(s,t):
    N=len(s)
    M=len(t)
    
    if M==0 or N==0 : return ''
    finalo=''
    fin=''
    
    
    for i in range(N):
        if s[i] in t:
            finalo=s[i]+lcs(s[i+1:],t[t.index(s[i])+1:])
            
        if len(finalo)> len(fin) or fin=='':
            fin=finalo
                
    return fin

print(lcs("AGCAT","GAC"))
print(lcs("The quick brown fox jumps over the lazy dog.","Pack my box with five dozen liqour jugs."))
        