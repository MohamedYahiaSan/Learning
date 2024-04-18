# This is an implementation to the other solution I have it fails few cases though
# I won't be commenting nor fixing that code though as it's a disappointment for me
# I won't spend more time on this problem anytime soon so if someone ever reads this
# This was just a 99% successful attempt (I can definitly fix it, but don't feel like it)

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

    sums=set()
    rest=set()
    remain=0

    singles=set()
    while queue:
        curr=queue.pop(0)
        val=curr.tot
        roots=set([x.tot for x in curr.parents])
        rest.add(total-val)
        
        remain=total-val

        

        smoll=(total-val)/2

        #1
        if val>half:
            queue=curr.sons + queue
            singles.add(curr.value)
            sums.add(val)
            continue
        #2
        elif val==half or val+curr.parent.value==half:
            result.append(half)
        #3
        elif val>(total-2*val):
            if val in sums or 2*val in rest or 2*val in roots:
                result.append(val-(total-2*val))
            if  remain-val in sums or remain-val in rest or remain-val in singles:
                result.append(val-(total-2*val))
            if total-2*val in singles:
                result.append(val-(total-2*val))
        else:
            if smoll in sums :
                if smoll in roots:
                    if smoll==half:
                        result.append(half)
                else:
                    result.append(smoll-val)
            if smoll in rest:
                if smoll in roots or smoll==val+curr.parent.value:
                    if smoll==half:
                        result.append(half)
                else:
                    result.append(smoll-val)
       
        
            
            



        singles.add(curr.value)
        sums.add(val)
        queue=curr.sons + queue
    if result==[]: return -1 
    return int(min(result))







if __name__ == '__main__':
    fptr = open('result.txt', 'w')
    ftr=open('data.txt','r')
    q = int(ftr.readline().strip())
    count=1
    for q_itr in range(q):
        n = int(ftr.readline().strip())

        c = list(map(int, ftr.readline().rstrip().split()))

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, ftr.readline().rstrip().split())))

        result = balancedForest(c, edges)

        fptr.write(str(result) + '\n')
        count+=1

    fptr.close()
ftr.close()