# Create the node
class Node:
    def __init__(self, next=None, prev=None, data=None):
        # referencing to the next node
        self.next = next
        # referencing to the previous node
        self.prev = prev
        self.data = data