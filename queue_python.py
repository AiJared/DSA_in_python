# Implementing a Queue using a list

class Queue:
    def __init__(self):
        self.items = []
    
    def enque(self, item):
        if not self.is_empty():
            return self.items.append(item)
        else:
            return "Queue is empty"
    
    