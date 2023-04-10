def can(s,arr,mem={}):
    if s in mem: return mem[s]
    N=len(s)
    M=len(arr)
    if N==0: return 1
    mem[s]=0
    
    for i in range(N):
        if s[:i+1] in arr:
            if can(s[i+1:],arr,mem):
                mem[s]+=1
            
    
    return mem[s]

print(can("abcdef",['abcdef','ab','cdef','ab','abc','cd','def','abcde','f','a','bcdef']))
#print(can('mohamed yahia',['ia','ah',' y','moha','med','mohamed']))
#print(can("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",['e','eeee','f','eeeeeeeee','ee']))