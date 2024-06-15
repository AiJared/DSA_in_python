# Representing a circular linked list in Python
class Node:
    def __init__(self, data=None):
        # Data stored in the node
        self.data = data
        # reference to the next node in the circular linked list
        self.next = None