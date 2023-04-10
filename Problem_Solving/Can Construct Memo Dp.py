def can(s,arr,mem={}):
    if s in mem: return mem[s]
    N=len(s)
    M=len(arr)
    if N==0 : return  True
    
    for i in range(N):
        if s[:i+1] in arr : 
            if can(s[i+1:],arr,mem):
                mem[s]=True
                return True
    
    
    mem[s]= False
    return mem[s]

print(can("abcdef",['ab','abc','cd','def','abcd']))
print(can('mohamed yahia',['ia','ah',' y','moha','med']))
print(can("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",['e','eeee','f','eeeeeeeee','ee']))