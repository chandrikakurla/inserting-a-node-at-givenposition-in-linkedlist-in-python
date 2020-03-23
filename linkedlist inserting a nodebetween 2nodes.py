class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    #pushingelements into linkedlist
    def push(self,newnode):
        if self.head is None:                      
            self.head=newnode
        else:
            temp=self.head
            self.head=newnode
            newnode.next=temp
    #inserting a node at given position
    def insert_node_between_2nodes(self,newnode,position):
        currentnode=self.head
        currentposition=0
        while True:
            if currentposition==position:
                previousnode.next=newnode
                newnode.next=currentnode
                break
            else:
                previousnode=currentnode
                currentnode=currentnode.next
                currentposition +=1
    #printing linkedlistelements            
    def print_llist(self):
        currentnode=self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode=currentnode.next
if __name__=='__main__':
    firstnode=Node(20)
    llist=LinkedList()
    llist.push(firstnode)
    secondnode=Node(10)
    llist.push(secondnode)
    thirdnode=Node(15)
    llist.insert_node_between_2nodes(thirdnode,1)
    llist.print_llist()
    

        
