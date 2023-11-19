class Solution:
    def findIntersection(self,head1,head2):
       
        
        new=None
        c1=head1
        c2=head2
        x= True

        if c1.next== None and c2.next==None:
            if c1.data==c2.data:
                new=Node(c1.data)
                return new
        elif c1.next== None and c2.next!=None:
            if c1.data==c2.data:
                new=Node(c1.data)
                return new
        elif c1.next!= None and c2.next==None:
            if c1.data==c2.data:
                new=Node(c1.data)
                return new
                
                
        while c1.data!= None or c2.data!=None:
            
            #print(c1.data,c2.data)

            if c1.data==c2.data and x:
                current=Node(c1.data)
                new=current
                prev=new
                #print(current)
                
                #print(current)
                if c1.next==None or c2.next==None:
                    break
                if c1.next!=None: c1=c1.next
                if c2.next!=None: c2=c2.next
                x=False
                
            elif c1.data==c2.data:
                current=Node(c1.data)
                prev.next=current
                prev=current
                #print(c1.data,c2.data)
                if c1.next==None or c2.next==None:
                    break
                if c1.next!=None: c1=c1.next
                if c2.next!=None: c2=c2.next
                #if current.data==987: print(c1.data,c2.data)
            
            

            elif c1.data<c2.data:
                if c1.next==None:
                    if c2.next!=None:
                        c2=c2.next
                    else:
                        break
                else:
                    if c1.next!=None: c1=c1.next
                                
            else:
                if c2.next==None:
                    if c1.next!=None:
                        c1=c1.next
                    else:
                        break
                else:
                    if c2.next!=None: c2=c2.next
            
                
        return new
    










class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=1
    for _ in range(t):
        with open('data.txt','r') as file:
            n1,n2=[int(x) for x in (file.readline().split())]
            arr1=[int(x) for x in (file.readline().split())]
            arr2=[int(x) for x in (file.readline().split())]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)
        ob = Solution()
        result = ob.findIntersection(ll1.head,ll2.head)
        printList(result)
        print()

# } Driver Code Ends