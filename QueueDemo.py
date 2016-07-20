class QueueDemo:
    
    def __init__(self):
        self.data = []
        
    def enque(self,item):
        self.data.insert(0,item)
        
    def deque(self):
        print "item removed is"
        self.data.pop()
        
    def display(self):
        print "Queue elements are"
        for item in self.data:
            print item
if __name__=='__main__':
    queue=QueueDemo()
    queue.enque(1)
    queue.enque(2)
    queue.enque(3)
    queue.display()
    queue.deque()
    queue.display()
