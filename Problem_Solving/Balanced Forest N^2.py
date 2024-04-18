#This is the solution to the problem balanced forest where we split the tree into 3 equal trees and add minimal value to achieve that if needed
#This approach is a bit messy and is O(N^2) which can be further optimizied
#by using a cach set to store values as we do DFS and using values stored there we calculate the result
#I am not going to explain this solution in detail as it's a bit messy and better one can be achieved
#Simply try to copy paste the same algorithm using a singel DFS and a set to solve it 

import math
import os
import random
import re
import sys
from collections import defaultdict as dd



class node:
    vault=dd(list)
    def __init__(self,value:int,sons,depth=0,parent=None):
        self.value=value
        self.sons=sons
        self.parent=parent
        self.depth=depth
        self.tot=0
        self.parents=[]
    
    
    @staticmethod
    def create_tree(elements,connections):
        for i in range(len(elements)):
            elements[i]=node(elements[i],[])
        for a,b in connections:
            A,B=elements[a-1],elements[b-1]
            A.sons+=[B]
            B.sons+=[A]
        root=elements[0]
        root.parent=None
        root.parents=[]
        root.depth=0
        node.vault[0]=[root]
        root.direct()
        return root
    
    def direct(self):
        self.tot=self.value
        for son in self.sons:
            son.sons=[x for x in son.sons if x!=self]
            son.parent=self
            son.parents=self.parents+[self]
            son.depth=self.depth+1
            node.vault[son.depth].append(son)
            son.direct()
            self.tot+=son.tot

    
    def print_tree(self):
        stack = [self]
        while stack:
            curr=stack.pop(0)
            if curr.parent==None: x=None
            else: x=curr.parent.value
            print(x,'<==',curr.value,'==>',[x.value for x in curr.sons],':',curr.depth)
            stack.extend(curr.sons)


def balancedForest(c, edges):
    if len(c)<2: return -1
    result=[]
    tree_head=node.create_tree(c,edges)
    total=tree_head.tot
    half=total/2
    
    queue=[tree_head]
    while queue:
        curr=queue.pop(0)
        val=curr.tot
        
        if val>half:
            queue=curr.sons.copy() + queue
            continue

        elif val==half:
            answer=val
            cond=1

        else:
            if  val > (total-2*val):
                answer=val
                cond=2
            else:
                answer=(total-val)/2
                cond=3
                if (total-val)%2!=0: 
                    queue=curr.sons.copy() +queue
                    continue
       

        loop=[tree_head]
        parents=curr.parents
        accum=0
        rest=0
        while loop:
            curr_2=loop.pop(0)
            val_2=curr_2.tot
            if curr_2== curr: continue
            if curr_2 in parents: val_2 -=val
            accum=val_2
            rest=total-accum-val

            if accum == answer or rest == answer:
                if cond==1:
                    res=half
                elif cond==2:
                    res=val - (total-2*val)
                elif cond==3:
                    res=answer-val
                result.append(res)
                break

            loop.extend(curr_2.sons)


        queue=curr.sons.copy() +queue

    if result==[]: return -1 
    return int(min(result))







if __name__ == '__main__':
    fptr = open('result.txt', 'w')
    ftr=open('data.txt','r')
    q = int(ftr.readline().strip())

    for q_itr in range(q):
        n = int(ftr.readline().strip())

        c = list(map(int, ftr.readline().rstrip().split()))

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, ftr.readline().rstrip().split())))

        result = balancedForest(c, edges)

        fptr.write(str(result) + '\n')

    fptr.close()
ftr.close()
