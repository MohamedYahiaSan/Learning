# Solution for Square Ten Tree problem without using gmpy2 (a bit slow)
# This code could be further solved with literally creating a class to handle the very large numbers, however I won't do that
import math 
import sys
from datetime import datetime

sys.set_int_max_str_digits(10000001)            # Adjusting size in system as we have million plus digits in test cases 

def count_zeros(str_num,last):                  # Counter to count zeros from right side    
    count=last[0]                               # Last is a store we store our last readings to continue counting from then 
    i=last[1]

    while str_num[-i] =='0':
        count+=1
        i+=1
    
    last[0]=count
    last[1]=i

    return count,last


f=open('data.txt','r')
l=int(f.readline())
r=int(f.readline())
f.close()

# Initializing some constants
result=[[0,0]]
i=0
num=l
if num!=0: num-=1
last=[0,1]                  
t1=datetime.now()
c=0

# Looping till we reach the r side 
while True:
    t2=datetime.now()
    # In this approach we use the number as a string to count zeros as this is faster then performing arthmitic operations on very large numbers with the default operators 
    str_num=str(num)
    print('Time to str(num)=',datetime.now()-t2)
    t2=datetime.now()

    if num==0:                                          # If num==0
        i=len(str(r))-1
        if i>0:
            i=int(math.floor(math.log2(i)+1))
        last=[0,1]

    

    elif str_num[-1] !="0":                             # If we had a no zero on right side 
        i=0


    else:                                               # If we have zeros that will need counting
        zeros,last=count_zeros(str_num,last)
        i=int(math.floor(math.log2(zeros)+1))

    print('calculating the next power of 10 time=',datetime.now()-t2)
    t2=datetime.now()

    if i>0:
        a= 10 ** (2 ** (i - 1))
        b= (10 ** (2 ** i))

        if num+a>r:
            r=r-num
            num=0
            continue
        
        to=min(r-num,b-num)

        repeat= to % b
        repeat= repeat // a
        num+= repeat * a

    else:
        last=[1,2]
        add=1
        temp=10-int(str_num[-1])
        temp=min(r-num,temp)
        repeat=temp
        num+= repeat * add

    if i==result[-1][0]:
        result[-1][1]+=repeat
    else:
        result.append([i,repeat])
    print('arthmitic operation time=',datetime.now()-t2)
    t2=datetime.now()

    c+=1
    if num==r:                              # If we found number then break 
        break


# Outputting the results
if result[0]==[0,0]:
    result=result[1:]

n=len(result)
t2=datetime.now()
print(t2-t1)

f=open('result.txt','w')
f.write(str(n))
for ele in result:
    line='\n'+ str(ele[0])+' '+ str( ele[1]) 
    f.write(line)
f.close()