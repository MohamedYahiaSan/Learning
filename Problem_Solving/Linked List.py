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
        
        
    #  Function to print the linked list
    def Plist(self):
        current=self.head
        while (current):
            print(current.data, end=" ++ ")
            current=current.next
        print()


# Testing 
test= LinkedList()
test.Plist()
test.add([1,2,3,4])
test.Plist()
test.add("Kishou")
test.add("Kishou San")
test.add(99)
test.Plist()
test.insert(5,4)
test.Plist()