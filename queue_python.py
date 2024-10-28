# Implementing a Queue using a list

class Queue:
    def __init__(self):
        self.items = []
    
    def enque(self, item):
        return self.items.append(item)
        
    
    def deque(self):
