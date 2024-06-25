# Creating the node
class Node:
    """
    A node stores the data item and a reference to the next node
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data
    

# Create a Singly Linked List
