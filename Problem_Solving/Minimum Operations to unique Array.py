# Mapping any given Arr into unique elements from 1 to n with the lowest possible operations of (+1 or -1)
from collections import defaultdict as dd
import pandas as pd

# Function to map the array
def Mapping(arr):
    #creating a default dictionary to help map the used integers. Initialized at False
    Map=dd(bool)

    # Creating a cache set to fill in the map. True for each existing int
    cache=set(arr)
    for ele in cache:
        Map[ele]=True
    
    #Operations counter
    operation=0

    #creating a sorted version of the array
    #Sorting the array will help us save time and get accurate results as we iterate and perform addition or substraction
    #As we trying to minimize the operation count
    A=sorted(arr)

    #resetting our cache set to store values as we iterate
    cache=set()

    #Iterating over the elements and fixing redundunt integers (moving them to the shortest empty location)
    #Where we deploy the Map we made earlier
    for i in range(len(A)):
        #If we found that the current Element has already been found before
        if A[i] in cache:
            #We start a loop that starts adding 1 or subbing 1 till we find the closest empty location
            j=1
            while True:
               #we priortize the substraction as to cause more room for upcoming elements
               #here the sorting we did comes in handy as we already know that all upcoming elements are bigger
               if A[i]-j >0 and Map[A[i]-j]==False: #we make sure it's empty in the Map and also >0
                   A[i]=A[i]-j                      #Updating the element if valid
                   Map[A[i]]=True                   #Updating the map
                   cache.add(A[i])                  #Updating the Cache
                   operation+=j                     #Adding the value to the operations count
                   break
               
               #if the substraction fails we go to the addition (note that we will always have room for subbing the biggest number n)
               elif Map[A[i]+j]==False:             #Since we using default dict, it will be false for any non recorded value
                   A[i]=A[i]+j                      #Updating the element if valid
                   Map[A[i]]=True                   #Updating the map
                   cache.add(A[i])                  #Updating the Cache
                   operation+=j                     #Adding the value to the operations count
                   break
               

               j+=1 #In case adding 1 or subbing 1 failed we move on to +2 or -2



        #in case the element wasn't encoutered before we add it
        else:
            cache.add(A[i])

    #returning the array and opeartions count as well as the Map
    return (A,operation,Map)

arr=list(map(int,input("Enter desired array sperated with spaces: 1 2 3 = [1,2,3]\n arr=").split()))

array,operations,Map=Mapping(arr)
Map=pd.Series(Map,index=[i for i in range(1,max(array)+1)])
Map.fillna(False,inplace=True)

print(array,operations,Map,sep='\n')


