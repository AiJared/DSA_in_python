# Implementing a Queue using a list

class Queue:
    # initialize an empty queue
    def __init__(self):
        self.items = []
    
    # add elements at the end of the queue
    def enque(self, item):
        return self.items.append(item)
        
    # remove the front elements of the queue
    def deque(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty!"
    
    # View the front element without removing it
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Queue is empty!"
    
    # check if the queue is empty
    def is_empty(self):
        return (self.items) == 0
    
    # check the size of the queue
    def size(self):
        return len(self.items)