class Stack:
    def __init__(self):
        self.items = []
    
    # Add elements ontop of the stack
    def push(self, item):
        self.items.append(item)
    
    # Remove elements from the top of the stack
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"
    
    # Check the topmost element without removing it
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"
    
    # Check if the stack is empty
    def is_empty(self):
        return (self.items) == 0
    
    # Check the size of the stack
    def size(self):
        return len(self.items)

# Instantiate a stack object
my_stack = Stack()

# Push elements to the class
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

# Check the topmost element
print(my_stack.peek())

# Pop elements off of the stack
print(my_stack.pop())

# Check the size of the stack
print(my_stack.size())