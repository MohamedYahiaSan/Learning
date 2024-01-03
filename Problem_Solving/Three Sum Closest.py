#Solving Three Sum Closest, using Sorting then 2 pointer algorithms
def threeSumClosest ( arr, target):
            #Function to be used as a 2-pointer
            def solve(arr,k,b,n,ind,diff,result):
                i,j=0,n-1 #Initializing our 2-pointers
                while j>i: #2pointer looping
                    #Skipping the current index from the outer function (no repeating)
                    if i==ind:
                        i+=1
                        continue
                    elif j==ind:
                        j-=1
                        continue
                    
                    #total sum of current pointers
                    a=arr[i]+arr[j]+b
                    temp=abs(k-a) #temprarory abs difference (our Gauge basically)

                    #print(f'3_sum={a}, abs diff={temp}, boolean={a>k}') #can be uncommented to help debugging
                    
                    #Comparision and choosing the closest highest value
                    if temp==diff:
                        result=max(a,result)
                    elif temp<diff:
                        diff=temp
                        result=a

                    #Pointers guide
                    if a>k:
                        j-=1
                    else:
                        i+=1
                    
                return result
            
            
            n=len(arr)
            result=float('-inf') #Initialized at -inf to be replaced later with highest values
            diff=float('inf')   #Initialized at inf to be replaced later with lowest values
            my_array=sorted(arr) #Sorting our array 
            
            #looping through the sorted array and taking one element (i=ind) then running 2-pointer on the remaining array
            for i in range(n):
                b=my_array[i]
                x=solve(my_array,target,b,n-1,i,diff,result) #Running 2 pointer 

                diff2=abs(target-x) #closeness gauge for outer function

                if diff2==0: return x
                
                #Comparision and choosing the closest highest value for outer function
                if diff2<diff:
                    diff=diff2
                    result=x
                elif diff2==diff:
                    diff=diff2
                    result=max(result,x)

            return result


#Driver code to read the input
t = int (input ())
for tc in range (t):
    n, target = list(map(int, input().split()));
    arr = list(map(int, input().split()));
    
    print (threeSumClosest (arr, target))