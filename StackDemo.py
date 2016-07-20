class StackDemo:

    def __init__(self):
        self.data = []
        
    def push(self,item):
        self.data.append(item)
        
    def pop(self):
        print "Poped top element"
        print self.data.pop()
        
    def display(self):
        print "Current Stack contents are"
        for item in self.data:
            print item
    
if __name__=='__main__':
    
    stack=StackDemo()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.display()
    stack.pop()
    stack.display()
    
    
