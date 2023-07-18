# Practicing on Linked list Nodes Tree
class node:
    def __init__(self, data):
        self.data = data
        self.next= None

class LinkedList:
    # Function to initialize head of linkedlist
    def __init__(self) -> None: 
        self.head = None    
    
    # Function to add data to the tail of the list
    def add(self,data):
        
        if self.head==None:
            self.head= node(data)
       
        else:
            current=self.head
            while current.next!= None:
                current=current.next
            current.next= node(data)
    
    
    # Function to insert data at an index (default at the begining of the list)
    def insert(self,data,n=0):
        if n==0:
            temp=self.head
            now=node(data)
            now.next=temp
            self.head=now

            return None
        now=self.head
        i=0
        while (i<n-1):
            now=now.next
            i+=1
        
        temp=now.next
        now.next=node(data)
        now=now.next
        now.next=temp
        
    
    #reverse function
    def Reverse(self):
        current=self.head
        prev= None
        while(current):
            tmp=current.next
            current.next = prev
            prev=current
            current=tmp         
        self.head=prev
        
    #Zipper function
    def Zip(self,second):
        current=self.head
        parralel=second.head
        
        while(current and parralel):
            tmpc=current.next
            tmpp=parralel.next
            current.next=parralel
            parralel.next=tmpc
            current=tmpc
            parralel=tmpp
            
        
    #  Function to print the linked list
    def Plist(self):
        current=self.head
        while (current):
            print(current.data, end=" ==> ")
            current=current.next
        print()


# Testing 
test= LinkedList()
test.Plist()
test.add(1)
test.Plist()
test.add(2)
test.add(3)
test.add(4)
test.Plist()
test.insert(5,4)
test.Plist()
test.Reverse()
test.Plist()
test2=LinkedList()

for i in range(6):
    test2.add(chr(97+i))

test.Reverse()   
test.Plist()
test2.Plist()
test.Zip(test2)
test.Plist()