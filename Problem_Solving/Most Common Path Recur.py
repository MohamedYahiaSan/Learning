def com(stack1,stack2,L=10):
    
    N=len(stack1)
    M=len(stack2)
    
    if M == 0 or N ==0 : 
        return 0
    
    max=0
    for i in range(N):
        result=0
        if stack1[i] in stack2:
            result=1+com(stack1[i+1:],stack2[stack2.index(stack1[i])+1:],len(stack1[i+1:]))
        
        if result>max:
            max=result
    return max 

print(com([5,1,4,3,7],[5,4,3,7,1],5))   