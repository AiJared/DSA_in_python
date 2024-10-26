class Stack:
    def __init__(self):
        self.items = []
    
    # Add elements ontop of the stack
    def push(self, item):
        self.items.append()
    
    # Remove elements from the top of the stack
    def pop(self):
        if not is_empty():
            self.items.pop()
        else:
            return "Stack is empty"
    
    # Check the topmost element without removing it
    def peek(self):
        if not is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"
    
    # Check if the stack is empty
    def is_empty(self):
        return (self.items) == 0
    