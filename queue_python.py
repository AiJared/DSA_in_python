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
    
# Create a queue object
queue = Queue()

# Add elements to the queue
queue.enque("a")
queue.enque("b")
queue.enque("c")

# View the front element without removing it
print(queue.peek())

# Remove the front element from the queue
print(queue.deque())

# Check the size of the queue
print(queue.size())