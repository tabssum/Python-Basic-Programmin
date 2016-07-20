class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def print_list(self):
        temp=self.head
        print temp
        while(temp):
            temp=temp.next  

        
if __name__ == "__main__":
    list_demo=LinkedList()
    list_demo.head=Node(1)
    print list_demo.head
    second=Node(2)
    third=Node(3)
    list_demo.head.next=second
    second.next=third
    list_demo.print_list()
    
