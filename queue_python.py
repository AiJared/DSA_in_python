# Implementing a Queue using a list

class Queue:
    def __init__(self):
        self.items = []
    
    def enque(self, item):
        return self.items.append(item)
        
    
    def deque(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"
    
    
        