from collections import defaultdict


#function to calculate the sum of pairs under the following conditions:
#the sum of f(a[i], a[j]) of all pairs (i, j) such that (1 <= i < j <= n).
#
#f(a[i], a[j]):       if abs(a[j]-a[i]) > 1
#
#                         f(a[i], a[j]) = a[j] - a[i]
#
#                         else  if abs(a[j]-a[i]) <= 1
#
#                         f(a[i], a[j]) = 0
def sum (arr, n) :    
    result_b=0
    map_sum=0
    
    # Initializing a frequency map and creating a sum for the array, sum(arr)
    after_map = defaultdict(int)

    for ele in arr:
        after_map[ele]+=1
        map_sum+= ele


    for i in range(n):
        
        #Calculating the number of times we need to deduce the element arr[i] from the total sum to achieve the f(a[i], a[j]) = a[j] - a[i] for all valid elements
        z= after_map[arr[i]]  + (n - i - after_map[arr[i]] - after_map[arr[i]+1] - after_map[arr[i]-1])


        #Adding to the result the correct sum, by removing the excess arr[i] and all elements that are either arr[i]+1 or arr[i]-1
        result_b+= map_sum - ( arr[i]*z + after_map[arr[i]+1]*(arr[i]+1) + after_map[arr[i]-1]*(arr[i]-1)  )


        #Removing current element from the map and the total sum
        map_sum-=arr[i]
        after_map[arr[i]]-=1


    
    
    return result_b



#Test Data creator code
import random
with open ('data.txt','w') as file:
    print(1,file=file)
    print(100000,file=file)
    for i in range(100000):
        x=random.randint(1,10**7)
        print(x,end=" ",file=file)
    
#Problem drive code
with open('data.txt','r') as file:
    t=int(file.readline())
    n=int(file.readline())
    arr=list(map(int, file.read().strip().split()))
    ans= sum(arr,n)
    print(ans)
    