def can(s,arr,mem={}):
    if s in mem : return mem[s]
    N=len(s)
    M=len(arr)
    if N==0 : return [[]]
    if M==0 : return [[]]
    here=[]
    
    for i in range(M):
        if arr[i] == s[:len(arr[i])]:
            here+=[[arr[i]]+ ele for ele in can(s[len(arr[i]):],arr)]
            
            
    mem[s]=here
    return mem[s]
        

print(can("abcdef",['ab','abc','cd','def','abcd','ef','c']))
print(can('mohamed yahia',['ia','ah',' y','moha','med','mohamed']))
#print(can("eeeeeeeeeeee",['e','eeee','f','eeeeeeeee','ee']))